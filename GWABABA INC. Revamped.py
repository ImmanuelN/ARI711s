#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import networkx as nx
import matplotlib.pyplot as plt

def total_distance(route, distances):
    total = 0
    for i in range(len(route) - 1):
        total += distances[route[i]][route[i + 1]]
    total += distances[route[-1]][route[0]]
    return total

def print_route(route, distances):
    print("City\tDistance")
    for i in range(len(route) - 1):
        print(f"{route[i]}\t{distances[route[i]][route[i + 1]]}")
    print(f"{route[-1]}\t{distances[route[-1]][route[0]]}")

distances = {
    'Dorado Park': {'Khomasdal': 7, 'Katutura': 20, 'Eros': 15, 'Klein Windhoek': 12},
    'Khomasdal': {'Dorado Park': 7, 'Katutura': 6, 'Eros': 14, 'Klein Windhoek': 18},
    'Katutura': {'Dorado Park': 20, 'Khomasdal': 6, 'Eros': 25, 'Klein Windhoek': 30},
    'Eros': {'Dorado Park': 15, 'Khomasdal': 14, 'Katutura': 25, 'Klein Windhoek': 2},
    'Klein Windhoek': {'Dorado Park': 12, 'Khomasdal': 18, 'Katutura': 30, 'Eros': 2}
}

# Create a NetworkX graph from the distances dictionary
G = nx.Graph(distances)

# Define the initial and final routes
initial_route = ['Dorado Park', 'Eros', 'Khomasdal', 'Katutura', 'Klein Windhoek']
final_route = ['Katutura', 'Khomasdal', 'Dorado Park', 'Klein Windhoek', 'Eros']

# Calculate the total distance for the final route
final_distance = total_distance(final_route, distances)

# Draw the initial route
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edges(G, pos, edgelist=[(initial_route[i], initial_route[i+1]) for i in range(len(initial_route)-1)], edge_color='r')
nx.draw_networkx_edges(G, pos, edgelist=[(initial_route[-1], initial_route[0])], edge_color='r')
plt.title("Initial Route")
plt.show()

# Draw the final route
nx.draw(G, pos, with_labels=True)
final_edges = [(final_route[i], final_route[i+1]) for i in range(len(final_route)-1)]
final_edges.append((final_route[-1], final_route[0]))
nx.draw_networkx_edges(G, pos, edgelist=final_edges, edge_color='g')
plt.title(f"Final Route (Total Distance: {final_distance})")
plt.show()

# Print the initial and final routes with distances
print("Initial Route:")
print_route(initial_route, distances)
print("\nFinal Route:")
print_route(final_route, distances)
print(f"\nTotal Distance: {final_distance}")


# In[ ]:




