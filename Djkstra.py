class Graph():
    
    def __init__(self, vertices):
        
        self.V = vertices
        self.graph = [[0 for columns in range (self.V)] for rows in range (self.V)]
        
    def Min(self, Present_dist, Shortest_path_Vertice):
        
        min = 1e7
        
        for i in range (self.V):
            if min > Present_dist[i] and Shortest_path_Vertice[i] == False:
                min = Present_dist[i]
                min_index = i
                
        return min_index
    
    def print(self, source, Present_dist):
        print("Path from " + str(source) + " to")
        for i in range (self.V):
            print(str(i) + " : " + str(Present_dist[i]))
    
    def Djkstra(self, source):
        
        Present_dist = [1e7] * self.V
        Present_dist[source] = 0
        Shortest_path_Vertice = [False] * self.V
        
        for i in range (self.V):
            pick_min_to_exc = self.Min(Present_dist, Shortest_path_Vertice)
            Shortest_path_Vertice[pick_min_to_exc] = True
            
            for v in range (self.V):
                if self.graph[pick_min_to_exc][v] > 0 and Present_dist[v] > Present_dist[pick_min_to_exc] + self.graph[pick_min_to_exc][v] and Shortest_path_Vertice[v] == False:
                    Present_dist[v] = Present_dist[pick_min_to_exc] + self.graph[pick_min_to_exc][v]
        
        self.print(source, Present_dist)
        
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		]

g.Djkstra(2)