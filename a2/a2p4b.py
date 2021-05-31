"""
ECE406, W'21, Assignment 2, Problem 3(b) 
Skeleton solution file.
"""

"""
You are not allowed to import anything. If we see any import
statement, you earn an automatic 0.
"""

def move(on_route, vertices, path, b):
    this_vertex = on_route[0]
    for route in vertices[this_vertex]:
        if route[0] == b:
            path.append([route[0], route[1] + on_route[1]])
        else:
            new_on_route = []
            new_on_route = [route[0], on_route[1]+route[1], on_route[2]+1]
            if new_on_route[2] < len(vertices):
                move(new_on_route, vertices, path, b)
    

def nshortestpaths(G, a, b):
    """
    You need to implement this method.

    You are certainly allowed to define any subroutines you want
    above this method in this file.

    We will test with inputs that match the spec only --- G will
    be a non-empty graph, i.e., at least one vertex, and a, b will
    be distinct valid vertices in G --- so that means G will have at
    least 2 vertices. Of course within those constraints, we could test
    for corner cases. E.g., a graph of no edges, e.g., G = [[],[],[]]
    """

    # get vertices from G
    vertices = []
    for vertex in G:
        vertices.append(vertex)

    path = []
    on_route = []

    for route in vertices[a]:
        if route[0] == b:
            path.append(route)
        else:
            on_route = route
            on_route.append(0)
            move(on_route, vertices, path, b)

    min_distance = 100000000
    count = 0
    for distinct_p in path:
        if distinct_p[1] < min_distance:
            count = 1
            min_distance = distinct_p[1]
        elif distinct_p[1] == min_distance:
            count += 1

    #print(path)
    return count


