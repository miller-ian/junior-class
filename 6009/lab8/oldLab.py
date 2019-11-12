"""6.009 Lab 7 -- Faster Gift Delivery."""


from graph import Graph

# NO ADDITIONAL IMPORTS ALLOWED!

class GraphFactory:
    """Factory methods to create instances of `Graph`."""

    def __init__(self, graph_class):
        """Initialize factory for `graph_class`."""
        self.cls = graph_class

    def from_list(self, adj_list, labels=None):
        """Create a graph from a simple adjacency list."""
        # Initialize.
        graph = self.cls()
        # Add nodes.
        for node in range(len(adj_list)):
            if labels is not None:
                graph.add_node(node, labels[node])
            else:
                graph.add_node(node)
        # Add edges.
        for node, neighbors in enumerate(adj_list):
            for neighbor in neighbors:
                graph.add_edge(node, neighbor)
        return graph

    def from_dict(self, adj_dict, labels=None):
        """Create a graph from a simple adjacency dictionary."""
        # Initialize.
        graph = self.cls()
        # Add nodes.
        for node in adj_dict:
            if labels is not None:
                graph.add_node(node, labels[node])
            else:
                graph.add_node(node)
        # Add edges.
        for node in adj_dict:
            for neighbor in adj_dict[node]:

                graph.add_edge(node, neighbor)
        return graph


class GraphHelpers:
    """Helper methods for the `Graph` implementations below."""

    @classmethod
    def permutations(cls, nodes, k, node_labels, pattern_labels, seen=set()):
        """Generate all node permutations matching the pattern labels."""
        if k == 0:
            return [[]]
        else:
            out = []
            for node in nodes - seen:
                if (pattern_labels[len(pattern_labels) - k]
                        not in ["*", node_labels[node]]):
                    continue
                for rest in cls.permutations(nodes, k - 1, node_labels,
                                             pattern_labels, seen | {node}):
                    out.append([node] + rest)
            return out



class FastGraph(Graph):
    """Faster implementation of `Graph`.

    Has extra optimizations for star and clique patterns.
    """

    def __init__(self):
        self.adjDict = dict()
        self.labels = dict()
    
    def eligible(self, node, sublist, pattern):
        #returns true if valid child of previous members of the sublist
        candidateNodeIndex = len(sublist)
        for i in range(len(sublist)):
            
            member = sublist[i]
            eligibleChildren = pattern[i][1]


            if candidateNodeIndex in eligibleChildren:
                if node not in self.adjDict[member]:
                    return False
        
        eligibleChildrenOfNodeIndex = pattern[candidateNodeIndex][1]
        for neighbor in eligibleChildrenOfNodeIndex:
            if neighbor < len(sublist):
                
                if sublist[neighbor] not in self.adjDict[node]:
                    return False       

        return True
             
    def get_candidates(self, unassignedLabel, aList):
        returnList = []
        possible = set()
        if unassignedLabel == '*':
            possible = self.adjDict.keys()
        elif unassignedLabel not in self.labels.keys():
            possible = set()
        else:
            possible = self.labels[unassignedLabel]
        for node in possible:
            if node not in aList:
                returnList.append(node)
        return returnList       

    def query(self, pattern, index=0, subList=None, returnList=None):
        if subList is None:
            subList = []
        if returnList is None:
            returnList = []
        if index == len(pattern):
            returnList.append(subList)
            return returnList
            
        unassignedLabel = pattern[index][0]
        candidates = self.get_candidates(unassignedLabel, subList)
        for candidate in candidates:
            otherList = subList.copy()
            if self.eligible(candidate, otherList, pattern):
                otherList.append(candidate)
                self.query(pattern, index+1, otherList, returnList)
                
        return returnList

        

    def add_node(self, name, label=''):
        """Add a node with name `name` and label `label`."""
        if name in self.adjDict.keys():
            raise ValueError
        else:
            self.adjDict[name] = []
            if label not in self.labels:
                self.labels[label] = set()
            self.labels[label].add(name)
    
    def remove_node(self, name):
        """Remove the node with name `name`."""
        if name not in self.adjDict.keys():
            raise LookupError
        else:
            for label in self.labels:
                self.labels[label].discard(name)
            del self.adjDict[name]
            for node in self.adjDict.keys():
                newList = []
                for edge in self.adjDict[node]:
                    if edge != name:
                        newList.append(edge)
                self.adjDict[node] = newList

    def add_edge(self, start, end):
        """Add a edge from `start` to `end`."""
        if start in self.adjDict.keys() and end in self.adjDict.keys():
            if end in self.adjDict[start]:
                raise ValueError
            else:
                theList = self.adjDict[start]
                theList.append(end)
                self.adjDict[start] = theList
        else:
            raise LookupError

    def remove_edge(self, start, end):
        """Remove the edge from `start` to `end`."""
        if start in self.adjDict.keys() and end in self.adjDict.keys():
            if end not in self.adjDict[start]:
                raise ValueError
            else:
                theList = self.adjDict[start]
                theList.remove(end)
                self.adjDict[start] = theList
        else:
            raise LookupError


if __name__ == '__main__':
    pass
