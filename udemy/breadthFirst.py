class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirst(self, array):
        queue = [self]
        print(queue)
        while len(queue) > 0:
            current = queue.pop(0)

            array.append(current.name)
            print(current.name)
            for child in current.children:
                queue.append(child)
        return array


node = Node(1)
node.addChild(2)
node.addChild(3)
node.addChild(4)
print(node.breadthFirst([5,[9,10],6,7]))


graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        #print(s, end = " ")
        for neighbor in graph[s]:
            print(s)
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
print(bfs(visited, graph, "A"))



from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):

        # mark vertices as not visited
        visited = [False] * (len(self.graph))

        queue = []

        # mark source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            #dequeue and print it
            s = queue.pop(0)
            print(s)

            #get all adjacent vertices



