class Graph:

    def __init__(self, vertices):
        self.V = vertices  # Virsuniu skaicius
        self.graph = []

    # funkcija pridet krastus

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # pagrindine MST funkcija
    def kruskal_mst(self):

        result = []  # MST rezultatas

        i = 0  # indexas rusiavimui
        e = 0  # Rezultatas rusiavimui

        # Isrusiuojam visas krastines didejimo tvarka pagal ju svori
        # Jei negalima pakeist duotojo grafiko, padarom jo kopija
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [];
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:

            # Paimam maziausia krastine ir padidinam indexa
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("Spausdinamos MST krastines: ")
        for u, v, weight in result:
            print("%d -- %d == %d" % (u, v, weight))

# Driver code


g = Graph(15)


g.add_edge(0, 1, 7)
g.add_edge(0, 3, 3)
g.add_edge(1, 2, 3)
g.add_edge(1, 4, 2)
g.add_edge(2, 5, 2)
g.add_edge(3, 4, 3)
g.add_edge(3, 6, 2)
g.add_edge(4, 5, 5)
g.add_edge(4, 7, 7)
g.add_edge(5, 8, 3)
g.add_edge(6, 7, 3)
g.add_edge(6, 9, 1)
g.add_edge(7, 8, 7)
g.add_edge(7, 10, 3)
g.add_edge(9, 12, 4)
g.add_edge(9, 10, 1)
g.add_edge(10, 11, 6)
g.add_edge(10, 13, 7)
g.add_edge(11, 12, 6)
g.add_edge(11, 14, 6)
g.add_edge(12, 13, 4)
g.add_edge(13, 14, 5)

g.kruskal_mst()