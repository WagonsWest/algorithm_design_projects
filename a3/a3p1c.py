"""
ECE406, W'21, Assignment 3, Problem 1(c) 
Skeleton solution file.
"""

"""
You are not allowed to import anything. If we see any import
statement, you earn an automatic 0.
"""

def cost(start, end, c):
    cost = float('inf')
    if str([start, end]) in c:
        cost = c[str([start, end])]
    return cost

def getCost(path, c):
    if len(path) == 1 or len(path) == 0:
        return 0
    
    totalCost = 0
    for i in range(len(path)-1):
        totalCost += cost(path[i], path[i+1], c)
    return totalCost

def robotpath(n, src, c):
    """
    You need to implement this method.

    You are certainly allowed to define any subroutines you want
    above this method in this file.

    We will test with inputs that match the spec only --- a string
    str([[a,b], [c,d]]) is a valid key of c if and only if a move
    [a,b] to [c,d] is valid. src is a valid source square, i.e.,
    s[0] == 1. You should return a list, which is a path from the src
    square to one of the destination squares that is the cheapest
    from src to one of the destination squares.
    """

    leastCost = float('inf')
    if src[0] == n:
        next_route = []
        next_route.append(src)
        return next_route

    next_route = []
    if src[1] != 1:
        next_src = [src[0]+1, src[1]-1]
        route_left = robotpath(n, next_src, c)
        cost_left = cost(src, next_src, c) + getCost(route_left, c)
        if cost_left < leastCost:
            leastCost = cost_left
            next_route = route_left

    if src[1] != n:
        next_src = [src[0]+1, src[1]+1]
        route_right = robotpath(n, next_src, c)
        cost_right = cost(src, next_src, c) + getCost(route_right, c)
        if cost_right < leastCost:
            leastCost = cost_right
            next_route = route_right
    
    next_src = [src[0]+1, src[1]]
    route_up = robotpath(n, next_src, c)
    cost_up = cost(src, next_src, c) + getCost(route_up, c)
    if cost_up < leastCost:
        leastCost = cost_up
        next_route = route_up

    next_route.insert(0, src)
    return next_route
