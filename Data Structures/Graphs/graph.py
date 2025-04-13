class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:

            if start in self.graph_dict:
                self.graph_dict[start].append(end)

            if start not in self.graph_dict:
                self.graph_dict[start] = [end]


    def get_paths(self, start, end, path=[]):
        # Always the path includes the starting node
        path = path + [start]

        if start ==  end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            
            # This means node not visited yet
            if node not in path:
                new_paths = self.get_paths(node, end, path)

                for p in new_paths:
                    paths.append(p)

        return paths

    def shortest_path(self, start, end, path=[]):

        path = path + [start]

        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)

                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp


        return shortest_path
    

    def all_shortest_paths(self, start, end):

        paths = self.get_paths(start, end)

        shortest_paths = []
        
        for p in paths:
        
        #finding the shortest path and comparing with each possible path found
            if len(p) == len(min(paths)):
                shortest_paths.append(p)
            

        return shortest_paths
        
         
        


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Dubai", "New york"),
        ("Paris", "New york"),
        ("New york", "Toronto")
    ]
    graph = Graph(routes)
    print(graph.graph_dict)
    start = "Mumbai"
    end = "New york"
    print(f"Paths between {start} and {end}", graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end}", graph.shortest_path(start, end))
    print(f"All Shortest paths between {start} and {end}", graph.all_shortest_paths(start, end))



# To understand get_paths function, see this recursion tree

# get_paths("Mumbai", "New york")
# ├── "Mumbai" → "Paris"
# │   └── get_paths("Paris", "New york")
# │       ├── "Paris" → "Dubai"
# │       │   └── get_paths("Dubai", "New york")
# │       │       └── "Dubai" → "New york"
# │       │           └── get_paths("New york", "New york") ✅ PATH FOUND: ['Mumbai', 'Paris', 'Dubai', 'New york']
# |       |                paths.append(['Mumbai', 'Paris', 'Dubai', 'New york'])
# │       └── "Paris" → "New york"
# │           └── get_paths("New york", "New york") ✅ PATH FOUND: ['Mumbai', 'Paris', 'New york']
# |                 paths.append(['Mumbai', 'Paris', 'New york'])
# └── "Mumbai" → "Dubai"
#     └── get_paths("Dubai", "New york")
#         └── "Dubai" → "New york"
#             └── get_paths("New york", "New york") ✅ PATH FOUND: ['Mumbai', 'Dubai', 'New york']
#                 paths.append(['Mumbai', 'Dubai', 'New york'])
