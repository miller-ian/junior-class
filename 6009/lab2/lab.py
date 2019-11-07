# NO IMPORTS ALLOWED!

import json

def did_x_and_y_act_together(data, actor_id_1, actor_id_2):
    for i in data:
        if actor_id_1 in i and actor_id_2 in i:
            return True
    return False

def get_collaborations_dictionary(data):
    #gets dictionary of all actors who worked with all other actors
    collabDict = {}
    for i in data:
        #parses data into first element and second element
        actor1 = i[0]
        actor2 = i[1]
        if actor1 == actor2:
            continue
        #adds each unique actor to the dictionary
        collabDict.setdefault(actor1, set()).add(actor2)
        collabDict.setdefault(actor2, set()).add(actor1)
    return collabDict

def get_children_bacon_number(collabDictionary, baconChildren, baconParents):
    nextGen = set()
    #for each actor in the current 'generation' of bacon number
    for actor in baconChildren:
        #for each individual actor in the dictionary created above that collaborated with the actor in the outer for loop
        for individual in collabDictionary[actor]:
            #if that actor is not in the above bacon level
            if individual not in baconParents:
                nextGen.add(individual)
                baconParents[individual] = actor
    newGen = set(nextGen)
    return newGen
                
def get_actors_with_bacon_number(data, n):
    initial = {4724}
    #Bacon would have no parents because he has a bacon number of 0
    initialParents = {4724: None}
    interactions = get_collaborations_dictionary(data)
    #finds all actors with a specfic bacon number
    for i in range(n):
        initial = get_children_bacon_number(interactions, initial, initialParents)
        
    return initial

def get_bacon_path(data, actor_id):
    return get_path(data, 4724, actor_id)

def determine_a_path(baconParents, actor1):
    final = []
    #finds the most efficient path
    while actor1 != None:
        final.append(actor1)
        actor1 = baconParents[actor1]
    #final will, at this point, be in reverse order because you are moving from the highest level to the lowest
    final.reverse()
    return(final)

def get_path(data, actor_id_1, actor_id_2):
    collabDictionary = get_collaborations_dictionary(data)
    #if either actor is not part of the data provided
    if(actor_id_1 not in collabDictionary):
        return None
    if(actor_id_2 not in collabDictionary):
        return None
    parents = {actor_id_1:None}
    currentLevel = {actor_id_1}
    #same process as finding bacon number
    while actor_id_2 not in currentLevel:
        #this line will alter currentLevel which in turn will alter parents
        currentLevel = get_children_bacon_number(collabDictionary, currentLevel, parents)
    end = determine_a_path(parents, actor_id_2)
    return end

def id_movie_mapping(dbMovies):
    final = {}
    #this creates a dictionary of movies and what actors acted in them
    for x, y in dbMovies.items():
        final[y] = x
    return final

def actor_pairs_in_movies(data):
    final = {}
    #this finds all movies that a pair of actors did together
    for actor1, actor2, movie in data:
        #frozenset is just an immutable version of a python set
        final[frozenset({actor1, actor2})] = movie
    return final

def get_movie_path(data, actor1, actor2):
    finalPath = []
    with open('resources/movies.json', 'r') as f:
        dbMovies = json.load(f)
    with open('resources/names.json', 'r') as f:
        dbNames = json.load(f)
    #finds a list of actors that connect two actors
    path = get_path(data, dbNames[actor1], dbNames[actor2])
    #maps actor ID's to movies
    idToMovie = id_movie_mapping(dbMovies)
    #maps actor pairs to movies to check for valid connections
    actorPairMovie = actor_pairs_in_movies(data)
    for i in range(len(path)-1):
        #finds the movie ID number for each valid pair of actors along the path
        mID = actorPairMovie[frozenset({path[i], path[i+1]})]
        finalPath.append(idToMovie[mID])
    return finalPath
        
def load_id(actor_name):
    with open('resources/names.json', 'r') as f:
        dbNames = json.load(f)
    return dbNames[actor_name]

def load_name(actor_id):
    with open('resources/names.json', 'r') as f:
        dbNames = json.load(f)
    for i in dbNames.keys():
        if actor_id == dbNames[i]:
            return i

if __name__ == '__main__':
    with open('resources/large.json') as f:
        smalldb = json.load(f)

    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.
    
    #print(load_name(934286))
    #print(did_x_and_y_act_together(smalldb, "Noureddine El Ati", "Randy Quaid"))
    i = load_id("Marion Davies")
    theList = get_bacon_path(smalldb, i)
    aList = []
    for i in theList:
        aList.append(load_name(i))
    print(aList)
    # theList = get_path(smalldb, load_id("Amy Meredith"), load_id("Apichart Chusakul"))
    # for i in theList:
    #     print(load_name(i))

