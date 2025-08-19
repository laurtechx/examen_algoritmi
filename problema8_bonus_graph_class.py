# Problema 8 – Bonus (15p) – Clasa Graph

from collections import deque
from typing import Dict, List

class Graph:
    def __init__(self):
        self.adj: Dict[str, List[str]] = {}

    def add_node(self, v: str):
        # TODO
        pass

    def add_edge(self, u: str, v: str, undirected: bool = True):
        # TODO
        pass

    def bfs(self, start: str) -> List[str]:
        # TODO
        return []

    def shortest_path(self, start: str, end: str) -> List[str]:
        # TODO
        return []

if __name__ == "__main__":
    g = Graph()
    # TODO: test
