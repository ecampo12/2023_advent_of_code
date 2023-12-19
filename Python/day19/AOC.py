import re
class Parts:
    cat_map = {}
    def __init__(self, x, m, a, s):
        self.cat_map = {'x': int(x), 'm': int(m), 'a': int(a), 's': int(s)}
    
    def __str__(self) -> str:
        return f"Part: {self.cat_map}"
        
def parse_input(input: str): 
    work_flow_map = {}
    parsed_parts = []
    workflows, parts = input.split("\n\n")
    flows = workflows.split("\n")
    for flow in flows:
        label, rules = re.findall(r"[^{|}]+", flow)
        rules = rules.split(",")
        work_flow_map[label] = rules
    
    parts = parts.split("\n")
    for part in parts:
        part = re.findall(r"[^{|}]+", part)[0]
        x, m, a, s = re.findall(r"\d+", part)
        parsed_parts.append(Parts(x, m, a, s))
        
    return work_flow_map, parsed_parts

def part1(work_flow_map, parts):
    accepted_parts = []
    for p in parts:
        key = "in"
        work_flow = work_flow_map["in"]
        sorted = False
        while not sorted:
            print(work_flow)
            for rule in work_flow:
                if '<' in rule:
                    category, rest = rule.split("<")
                    val, dest = rest.split(":")
                    if p.cat_map[category] < int(val):
                        if dest == 'A':
                            print(f"Accepted: {p}")
                            accepted_parts.append(p)
                            sorted = True
                            break
                        elif dest == 'R':
                            print(f"Rejected: {p}")
                            sorted = True
                            break
                        else:
                            work_flow = work_flow_map[dest]
                            print(f"From: {key} New work flow: {dest}")
                            key = dest
                            break
                elif '>' in rule:
                    category, rest = rule.split(">")
                    val, dest = rest.split(":")
                    if p.cat_map[category] > int(val):
                        if dest == 'A':
                            print(f"Accepted: {p}")
                            accepted_parts.append(p)
                            sorted = True
                            break
                        elif dest == 'R':
                            print(f"Rejected: {p}")
                            sorted = True
                            break
                        else:
                            work_flow = work_flow_map[dest]
                            break
                elif rule == 'R':
                    print(f"Rejected: {p}")
                    sorted = True
                    break
                elif rule == 'A':
                    print(f"Accepted: {p}")
                    accepted_parts.append(p)
                    sorted = True
                    break
                else:
                    print(f"New work flow: {rule}")
                    work_flow = work_flow_map[rule]
                    break
                    
    print(len(accepted_parts))
    total = 0
    for p in accepted_parts:
        total += sum(list(p.cat_map.values()))
    print(total)
    return total

def part2(input):
    return True

def main():
    input = open("input.txt", "r").read()
    w, p = parse_input(input)
    part1_sum = part1(w, p)
    part2_sum = 0
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()