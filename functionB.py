import random

def random_route(cities):
    route = list(cities)
    random.shuffle(route)
    return route