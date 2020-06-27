"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """

    def connectedSet(self, nodes):
        # DFS + 访问字典（标记一个点是否被访问过）
        if not nodes:
            return []

        components = []
        visited = set()
        for node in nodes:
            if node.label not in visited:
                self.findComponent(node, [], components, True, visited)

        return components

    def findComponent(self, node, component, components, isAddToComponents, visited):
        component.append(node.label)
        visited.add(node.label)
        for nei in node.neighbors:
            if nei.label not in visited:
                self.findComponent(nei, component, components, False, visited)

        if isAddToComponents:
            component.sort()
            components.append(component)
