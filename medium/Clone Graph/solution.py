# Time complexity: O(n) where n is number of nodes
# Approach: Recursively creating nodes.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.gmap = {}
    
    def setupGraph(self, oldNode, newNode):
        for i in range(len(oldNode.neighbors)):
            node = oldNode.neighbors[i]
            if node.val not in self.gmap:
                self.gmap[node.val] = Node(node.val)
                node2 = self.gmap[node.val]
                newNode.neighbors.append(node2)
                self.setupGraph(node, node2)
            else:
                node2 = self.gmap[node.val]
                newNode.neighbors.append(node2)
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        head = Node(node.val)
        self.gmap[node.val] = head
        self.setupGraph(node, head)
        return head