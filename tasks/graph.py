from typing import Any

__all__ = (
    'Node',
    'Graph'
)

# Hello actions

class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root


    def dfs(self) -> list[Node]:
        res = [self._root]
        for i in self._root.outbound:
            if i not in res:
                res.append(i)
                Graph.dfs_r(i, res)
        print('Res: ', res)   
        return res


    def dfs_r(node, res: list):
        l = list()
        for i in node.outbound:
            if i not in res:
                res.append(i)
                Graph.bfs_r(i, res)

#------------------------------------------------------------------------------------------------------

    def bfs(self) -> list[Node]:
        res = [self._root]
        res.extend(self._root.outbound)
        for i in self._root.outbound:
            Graph.bfs_r(i, res)
        print('Res: ', res)   
        return res


    def bfs_r(node, res: list):
        l = list()
        for i in node.outbound:
            if i not in res:
                l.append(i)
                res.append(i)
        for i in l:   
            Graph.bfs_r(i, res)

