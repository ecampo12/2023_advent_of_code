import networkx as nx
from time import perf_counter

def parse_input(input):
    graph = nx.Graph()
    for line in input:
        component, other = line.split(": ")
        other = other.split(" ")
        graph.add_node(component)
        for o in other:
            graph.add_edge(component, o)
    return graph

# Now that I had some sleep, I realized that netwrorkx has a function for this
# This runs a lot slower than the previous solution, but it's more general
def part1(graph):
    nodes = nx.minimum_edge_cut(graph)
    graph.remove_edges_from(nodes)
    g1, g2 = nx.connected_components(graph)
    return len(g1) * len(g2)

def main():
    input = open("input.txt", "r").read().splitlines()
    t1 = perf_counter()
    part1_sum = part1(parse_input(input))
    t2 = perf_counter()
    print(f"Part 1: {part1_sum}")
    print(f'It took {t2-t1} seconds to compute the solution')

if __name__ == "__main__":
    main()