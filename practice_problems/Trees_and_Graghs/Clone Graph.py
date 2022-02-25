class Node(object):
    def __init__(self,val,neighbors):
        self.val=val
        self.neighbors=neighbors

class Solution(object):
    def __init__(self):
        self.visited = {}

    # Time complexity O(N+M) N is a number of nodes(vertices and M is a number of edges)
    # Space complexity O(N)
    def cloneGragh(self,node):
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val,[])

        self.visited[node] = clone_node

        if node.neighbors:
            [self.cloneGragh(n) for n in node.neighbors]
        return clone_node