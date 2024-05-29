# Benchmarks subgraph isomorphism algorithms

# Generate 1000 graph / subgraph / mapping sets

# A mapping is between two isomorphic graphs A and B. Data type is a dictionary.
# mapping[a] = b, where a is a node of A that is isomorphically mapped to node b of B

from itertools import combinations, groupby
import networkx as nx
from networkx.algorithms import isomorphism
from itertools import tee
import random

graphs = []
subgraphs = []
mappings = []

# Number of graphs to test
n_test = 10

'''
 Function to create a graph A, subgraph B, and their mapping
 INPUT: n_a = number of nodes in graph A
        n_b = number of nodes in graph B
        n_a > n_b
'''

# Create a pair of isomorphic graphs
def createPair(n_a, n_b):
    # Create a random connected graph A
    A = gnp_random_connected_graph(n_a,p=0.1)

    # Random walk over A
    for i in nx.generate_random_paths(A, 1,path_length=n_b-1):
        # Generate graph
        edge_list = [pair for pair in pairwise(i)]
        B = nx.Graph()
        B.add_edges_from(edge_list)
    
    #Return the subgraph isomorphism
    GM = isomorphism.GraphMatcher(A, B)

    return A, B, GM

def gnp_random_connected_graph(n, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G

# Converts path into a list of edges
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

n_a = 100
n_b = 10

for n in range(n_test):
    A, B, GM = createPair(n_a,n_b)
    print("A", A)
    print("B", B)
    print("Isomorphic? ", GM.subgraph_is_isomorphic())

