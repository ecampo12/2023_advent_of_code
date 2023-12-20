import re
class Parts:
    def __init__(self, x, m, a, s):
        self.cat_map = {}
        self.cat_map = {'x': int(x), 'm': int(m), 'a': int(a), 's': int(s)}

class WorkFlow:
    class Rule: # Doesn't need to be an inner class, but whatever
        def __init__(self, rule):
            eq, self.next = rule.split(":")
            if "<" in rule:
                self.op = "<"
                self.key, self.val = eq.split("<")
                self.val = int(self.val)
            elif ">" in rule:
                self.op = ">"
                self.key, self.val = eq.split(">")
                self.val = int(self.val)
        
    def __init__(self, label, rules):
        self.rules = []
        self.label = label
        rules = rules.split(",")
        self.default = rules[-1]
        for rule in rules[:-1]:
            self.rules.append(self.Rule(rule))
    
    def eval_part(self, part: Parts):
        for rule in self.rules:
            # eval is bad, but it's the easiest way to do this
            if eval(f"part.cat_map[rule.key] {rule.op} rule.val"):
                return rule.next
        else:
            return self.default

def parse_input(input: str): 
    work_flow_map = {}
    parsed_parts = []
    workflows, parts = input.split("\n\n")
    flows = workflows.split("\n")
    for flow in flows:
        label, rules = re.findall(r"[^{|}]+", flow)
        work_flow_map[label] = WorkFlow(label, rules)
    
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
        while True:
            work_flow = work_flow_map[key]
            key = work_flow.eval_part(p)

            if key == "A":
                accepted_parts.append(p)
                break
            elif key == "R":
                break
    total = 0
    for p in accepted_parts:
        total += sum(list(p.cat_map.values()))
    return total

def find_ranges(work_flow_map, ranges, label="in"):
    if label == "R":
        return 0
    if label == "A":
        prod = 1
        for start, end in ranges.values():
            prod *= (end - start) + 1
        return prod
        
    workflow = work_flow_map[label]
    total = 0
    for rule in workflow.rules:
        start, end = ranges[rule.key]
        if "<" == rule.op:
            new_ranges = (start, min(rule.val - 1, end))
            rest = (max(start, rule.val), end)
        else:
            new_ranges = (max(start, rule.val + 1), end)
            rest = (start, min(rule.val, end))
            
        if new_ranges[0] <= new_ranges[1]:
            copy = dict(ranges)
            copy[rule.key] = new_ranges
            total += find_ranges(work_flow_map, copy, rule.next)
        if rest[0] <= rest[1]:
            ranges = dict(ranges)
            ranges[rule.key] = rest
        else:
            break
    else:
        total += find_ranges(work_flow_map, ranges, workflow.default)
    return total

def part2(work_flow_map):
    m = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    return find_ranges(work_flow_map, m)

def main():
    input = open("input.txt", "r").read()
    w, p = parse_input(input)
    part1_sum = part1(w, p)
    part2_sum = part2(w)
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()