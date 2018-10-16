"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if not vertex_id in self.vertices:
            self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            if not v1 in self.vertices[v2].edges:
                self.vertices[v1].edges.add(v2)
                self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")


class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 20 - 10
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 20 - 10
        else:
            self.y = y
            
    def __repr__(self):
        return f"{self.edges}, x = {round(self.x, 2)}, y = {round(self.y, 2)}"