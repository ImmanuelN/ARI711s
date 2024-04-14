def swap_cities(route, i, j):
    route[i], route[j] = route[j], route[i]
    return route

def neighbours(route):
    n = len(route)
    for i in range(n - 1):
        for j in range(i + 1, n):
            yield swap_cities(route.copy(), i, j)