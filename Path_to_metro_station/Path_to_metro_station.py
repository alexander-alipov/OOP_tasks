class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2, dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist

    def __hash__(self):
        return hash((self.v1, self.v2))

    def __eq__(self, other):
        return (self.v1 == other.v1 and self.v2 == other.v2) or (self.v1 == other.v2 and self.v2 == other.v1)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, dist):
        self._dist = dist


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if not v in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if not link in self._links:
            self._links.append(link)
            link.v1.links.append(link)  # добавление связанной вершины с v1
            link.v2.links.append(link)  # добавление связанной вершины с v2
            self.add_vertex(link.v1)  # добавление в общий список v1, если отсутствует
            self.add_vertex(link.v2)  # добавление в общий список v2, если отсутствует

    def dijkstra(self, start_v):
        self._V = len(self._vertex)
        self.start_v = start_v
        predecessors = {node: None for node in self._vertex}
        values = [1e7] * self._V
        passed_vertices = [False] * self._V
        vert_indx = self._vertex.index(start_v)
        passed_vertices[vert_indx] = True
        values[vert_indx] = 0
        dist = 0

        for count in range(self._V):
            adj = {v: (0, None) for v in range(self._V)}
            for link in self.start_v.links:
                adj[self._vertex.index(link.v2)] = (link.dist, link)
                adj[self._vertex.index(link.v1)] = (link.dist, link)

            minimum = 1e7
            for v in range(self._V):
                if adj[v][0] > 0 and passed_vertices[v] == False and values[v] > dist + adj[v][0]:
                    values[v] = dist + adj[v][0]
                    predecessors[self._vertex[v]] = (self.start_v, adj[v][1])
                if values[v] < minimum and passed_vertices[v] == False:
                    minimum = values[v]
                    vert_indx = v

            passed_vertices[vert_indx] = True
            self.start_v = self._vertex[vert_indx]
            dist = values[vert_indx]

        return predecessors

    def find_path(self, start_v, stop_v):
        predecessors = self.dijkstra(start_v)
        path = []
        path_links = []
        path.append(stop_v)
        current_node = predecessors[stop_v]
        while current_node:
            path_links.append(current_node[1])
            path.append(current_node[0])
            current_node = predecessors[current_node[0]]

        path.reverse()
        path_links.reverse()

        return path, path_links


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)
