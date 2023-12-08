import re

file = open("input.txt", "r")
input = file.read().splitlines()
file.close()

instructions = [0 if c == 'L' else 1 for c in input[0]]

routes = {}
a = []
z = []
for i in range(2, len(input)):
    x = re.findall(r"\w+", input[i])
    routes[x[0]] = (x[1], x[2])
    if x[0].endswith('A'):
        a.append(x[0])
    if x[0].endswith('Z'):
        z.append(x[0])
        
print(f"Nodes that end with \'A\': {a}")
print(f"Nodes that end with \'Z\': {z}")  

curr_inst = instructions[0]
counts = []
curr_inst = instructions[0]
z_seen = {}
for node in a:
    z_find = 3
    curr_loc = node
    cycle = []
    count = 1
    seen = []
    while z_find > 0:
        curr_loc = routes[curr_loc][curr_inst]
        curr_inst = instructions[count%len(instructions)]
        count += 1
        if curr_loc.endswith('Z'):
            z_find -= 1
            cycle.append(count-1)
            seen.append(curr_loc)
            
    z_seen[node] = seen
    counts.append(cycle)
for node in a:
    print(f"{node}: ")
    for end, count in zip(z_seen[node], counts[a.index(node)]):
        print(f"\tsaw: {end} after {count} steps")


