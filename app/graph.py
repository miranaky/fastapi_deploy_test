from collections import defaultdict


class Graph:
    def __init__(self, nodes):
        self.graph = defaultdict(list)
        self.N = nodes

    def addEdge(self, source_node_id, target_node_id):
        self.graph[source_node_id].append(target_node_id)

    def topologicalSortUtil(self, node, visited, stack):

        # mark the current node as visited
        visited[node] = True
        # recur for all nodes adjacent to this node
        for i in self.graph[node]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, node)

    def topologicalSort(self):
        visited = defaultdict(bool)
        stack = []

        for i in self.N:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        return stack


if __name__ == "__main__":
    g = Graph(["1", "2", "3", "4", "5", "6"])
    # g.addEdge("5", "2")
    # g.addEdge("2", "1")
    # g.addEdge("1", "4")
    # g.addEdge("1", "3")
    # g.addEdge("3", "6")
    # g.addEdge("4", "6")
    g.addEdge("2", "5")
    g.addEdge("1", "2")
    g.addEdge("4", "1")
    g.addEdge("3", "1")
    g.addEdge("6", "3")
    g.addEdge("6", "4")
    print("topological sort")

    print(g.topologicalSort())
