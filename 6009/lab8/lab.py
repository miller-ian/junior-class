"""6.009 Lab 8: Graphs, Paths, Matrices."""

from abc import ABC, abstractmethod
# NO ADDITIONAL IMPORTS ALLOWED!


class Graph(ABC):
    """Interface for a mutable directed, weighted graph."""

    @abstractmethod
    def add_node(self, node):
        """Add a node to the graph.

        Arguments:
            node (str): the node to add

        Raises:
            ValueError: if the node already exists.

        """

    @abstractmethod
    def add_edge(self, start, end, weight):
        """Add a directed edge to the graph.

        If the edge already exists, then set its weight to `weight`.

        Arguments:
            start (str): the node where the edge starts
            end (str): the node where the edge ends
            weight (int or float): the weight of the edge, assumed to be a nonnegative number

        Raises:
            LookupError: if either of these nodes doesn't exist

        """

    @abstractmethod
    def nodes(self):
        """Return the nodes in the graph.

        Returns:
            set: all of the nodes in the graph

        """

    @abstractmethod
    def neighbors(self, node):
        """Return the neighbors of a node.

        Arguments:
            node (str): a node name

        Returns:
            set: all tuples (`neighbor`, `weight`) for which `node` has an
                 edge to `neighbor` with weight `weight`

        Raises:
            LookupError: if `node` is not in the graph

        """

    @abstractmethod
    def get_path_length(self, start, end):
        """Return the length of the shortest path from `start` to `end`.

        Arguments:
            start (str): a node name
            end (str): a node name

        Returns:
            float or int: the length (sum of edge weights) of the path or
                          `None` if there is no such path.

        Raises:
            LookupError: if either `start` or `end` is not in the graph

        """

    @abstractmethod
    def get_path(self, start, end):
        """Return the shortest path from `start` to `end`.

        Arguments:
            start (str): a node name
            end (str): a node name

        Returns:
            list: nodes, starting with `start` and, ending with `end`, which
                  comprise the shortest path from `start` to `end` or `None`
                  if there is no such path

        Raises:
            LookupError: if either `start` or `end` is not in the graph

        """

    @abstractmethod
    def get_all_path_lengths(self):
        """Return lengths of shortest paths between all pairs of nodes.

        Returns:
            dict: map from tuples `(u, v)` to the length of the shortest path
                  from `u` to `v`

        """

    @abstractmethod
    def get_all_paths(self):
        """Return shortest paths between all pairs of nodes.

        Returns:
            dict: map from tuples `(u, v)` to a list of nodes (starting with
                  `u` and ending with `v`) which is a shortest path from `u`
                  to `v`

        """


class AdjacencyDictGraph(Graph):
    """A graph represented by an adjacency dictionary."""

    def __init__(self):
        """Create an empty graph."""
        raise NotImplementedError


class AdjacencyMatrixGraph(Graph):
    """A graph represented by an adjacency matrix."""

    def __init__(self):
        """Create an empty graph."""
        raise NotImplementedError


class GraphFactory:
    """Factory for creating instances of `Graph`."""

    def __init__(self, cutoff=0.5):
        """Create a new factory that creates instances of `Graph`.

        Arguments:
            cutoff (float): the maximum density (as defined in the lab handout)
                            for which the an `AdjacencyDictGraph` should be
                            instantiated instead of an `AdjacencyMatrixGraph`

        """
        raise NotImplementedError

    def from_edges_and_nodes(self, weighted_edges, nodes):
        """Create a new graph instance.

        Arguments:
            weighted_edges (list): the edges in the graph given as
                                   (start, end, weight) tuples
            nodes (list): nodes in the graph

        Returns:
            Graph: a graph containing the given edges

        """
        raise NotImplementedError


def get_most_central_node(graph):
    """Return the most central node in the graph.

    "Most central" is defined as having the shortest average round trip to any
    other node.

    Arguments:
        graph (Graph): a graph with at least one node from which round trips
                       to all other nodes are possible

    Returns:
        node (str): the most central node in the graph; round trips to all
                    other nodes must be possible from this node

    """
    raise NotImplementedError


if __name__ == "__main__":
    # You can place code (like custom test cases) here that will only be
    # executed when running this file from the terminal.
    pass
