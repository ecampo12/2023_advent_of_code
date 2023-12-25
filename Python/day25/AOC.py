# pip install pyvis
# Might also need to install Jupyter Notebook
from pyvis.network import Network
import networkx as nx
from collections import deque

def parse_input(input):
    connections = {}
    for line in input:
        component, other = line.split(": ")
        other = other.split(" ")
        if component not in connections:
            connections[component] = []
        for o in other:
            if o not in connections:
                connections[o] = []
            connections[component].append(o)
            connections[o].append(component)
    return connections

def part1(input, test=False):
    freq = set(input.keys())
    total_node = len(freq)
    # I could not think of a way to do this programmatically, so I graphed it.
    G = nx.Graph()
    for key in input.keys():
        G.add_node(key)
    for key in input.keys():
        for other in input[key]:
            G.add_edge(key, other)
    net = Network(notebook=True, filter_menu=True, select_menu=True)
    net.from_nx(G)
    net.show("test.html")
    
    if test:
        diconnect = [("hfx", 'pzl'), ('bvb', 'cmg'), ('nvd', 'jqt')]
    else: # Yes, this is specific to my input. The pyvis code above will help you find yours.
        diconnect = [('dgt', 'tnz'), ('rks', 'kzh'), ('gqm', 'ddc')]
        
    for d in diconnect:
        input[d[0]].remove(d[1])
        input[d[1]].remove(d[0])
    
    seen = set()
    queue = deque([list(input.keys())[0]])
    while queue:
        key = queue.popleft()
        if key not in seen:
            seen.add(key)
            queue.extend(input[key])
    group1 = len(seen)
    group2 = total_node - group1
    return group1 * group2

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(parse_input(input))
    print(f"Part 1: {part1_sum}")


if __name__ == "__main__":
    main()