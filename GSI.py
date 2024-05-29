# Python implementation of the algorithm described here: https://arxiv.org/pdf/1906.03420
'''
Definition 3 (Subgraph Isomorphism Search) Given query
graph Q and data graph G, the subgraph isomorphism search
problem is to find all subgraphs G' of G such that G' is
isomorphic to Q. G' is called a match of Q.
'''

'''
Inputs: G = Data graph, NetworkX object
        Q = Query graph, NetworkX object
Output: Mapping if any
'''

def GSI(Q,G):
    return -1