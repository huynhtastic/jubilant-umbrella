"""
Lesson 7
7/13/2016
    TREES - data connected through branches
            data structure
            appl in graph theory, game theory
    BRANCHES - the connection between nodes
    child
    sibling
    decendents: the child of the ancestor's child's child...
    ancestor:node that you would traverse to get to root,
                which is ancestor to all nodes
    internal node: has at least 1 chhild
    external node: same as leaf
    leaf
    sub tree: any tree that you can make within tree
    edge/vertex: nodes
    path: path connection btw nodes and edges w/ decendent
    level: 1+number of nodes it's decended from (1+# of branches it's decended from)
    height of a node: number of edges on longest path b/w that node and LEAF
    height of a tree: height of it's root node, number of branches
    Depth: number of edges form the node to the tree's root node
    Forest: set of n>= 0 DISJOINT trees
"""
#define node
class Node(object):
    def __init__(self):
        self.data = None
        s3