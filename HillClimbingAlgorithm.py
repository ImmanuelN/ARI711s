
import random
def random_route(cities):
    route = list(cities)
    random.shuffle(route)
    return route

def total_distance(route, distances):
    total = 0
    for i in range(len(route) - 1):
        total += distances[route[i]][route[i + 1]]
    total += distances[route[-1]][route[0]]
    return total

def neighbours(route):
    n = len(route)
    for i in range(n - 1):
        for j in range(i + 1, n):
            yield swap_cities(route.copy(), i, j)

def swap_cities(route, i, j):
    route[i], route[j] = route[j], route[i]
    return route

def hill_climbing(distances, max_iterations):
    route = random_route(distances.keys())
    current_distance = total_distance(route, distances)

    for _ in range(max_iterations):
        best_distance = current_distance
        for neighbour in neighbours(route):
            neighbour_distance = total_distance(neighbour, distances)
            if neighbour_distance < best_distance:
                route = neighbour
                current_distance = neighbour_distance
                break

    return route, current_distance