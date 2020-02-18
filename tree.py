from manimlib.imports import *

class Tree(VGroup):
    CONFIG = {
        "node_config": {
            "color": GREEN
        },
        "edge_config": {
            "color": BLUE
        },
        "from_zero": True
    }

    def __init__(self, n=10, **kwargs):
        digest_config(self, kwargs)
        self.edges = []
        self.G = [[] for _ in range(n + 1)]
        self.all_mobjects = self.graph_to_mobject()
        VGroup.__init__(*self.all_mobjects)
    
    def add_edge(self, f, t, v=0):
        self.edges.append([f, t, v])
        self.edges.append([t, f, v])
        m = len(self.edges)
        self.G[t].append(m - 1)
        self.G[f].append(m - 2)
    
    def graph_to_mobject(self):
        pass




class Test_tree(Scene):
    def construct(self):
        test = Tree()
        test.add_edge(0, 1)
        test.add_edge(0, 2)
        test.add_edge(1, 3)
        print(test.edges)
        print(test.G)
