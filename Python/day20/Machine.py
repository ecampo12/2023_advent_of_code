from dataclasses import dataclass
from math import lcm
from collections import deque
# F it I'm doing it in a class
class Machine: 
    # Trying out dataclasses, I like them.
    @dataclass
    class Module:
        name: str
        outputs: [str]
        isConjunction: bool = False
        
        def __post_init__(self):
            if self.isConjunction:
                self.state = {} 
            else:
                self.state = "off"
    
    def __init__(self, input: [str]):
        self.modules = {}
        
        for line in input:
            name, outputs = line.strip().split(" -> ")
            outputs = outputs.split(", ")
            match name[0]: # Apparently Python has switch statements now. Neat.
                case "%":
                    self.modules[name[1:]] = self.Module(name[1:], outputs)
                case "&":
                    self.modules[name[1:]] = self.Module(name[1:], outputs, True)
                case _:
                    self.broadcast = outputs
      
        for name, module in self.modules.items():
            for output in module.outputs:
                if output in self.modules and self.modules[output].isConjunction:
                    self.modules[output].state[name] = "low"
        
    def __repr__(self):
        return f"broadcast: {self.broadcast} {str(self.modules)}"
    
    def start_broadcast(self, loop = 1):
        low, high = 0, 0
        for _ in range(loop):
            low += 1
            queue = [("broadcaster", dest, "low") for dest in self.broadcast]
            while queue:
                origin, target, pulse = queue.pop()
                if pulse == "low":
                   low += 1
                else:
                    high += 1
                # There's a label 'rx' in the input thats not a module?? Probably somethiing for part 2.
                if target not in self.modules:
                    continue
                
                module = self.modules[target]
                if module.isConjunction:
                    module.state[origin] = pulse
                    outgoing = "low" if all(x == "hi" for x in module.state.values()) else "hi"
                    for x in module.outputs:
                        queue.append((module.name, x, outgoing))
                else:
                    if pulse == "low":
                        module.state = "on" if module.state == "off" else "off"
                        outgoing = "hi" if module.state == "on" else "low"
                        for x in module.outputs:
                            queue.append((module.name, x, outgoing))            
        return low * high
    
    def start_RX(self):
        # We find the module that has rx as an output. It seems to just be one and it is a conjunction.
        rx = [name for name, module in self.modules.items() if "rx" in module.outputs]
        rx = rx[0]
        # print(rx)
        
        # We find all the modules that lead to the the module that has rx as an output.
        rx_targets = {name: 0 for name, module in self.modules.items() if rx in module.outputs} 
        # print(rx_targets)
        
        # There seem to be four of them, and they're all conjunctions. They are all input to the 
        # previously foundconjunction, meaning we need to find when they all have a high pulse.
        # So far this seem like the same problem as Day 8, part 2.
        # We find the cycle length of each of the four modules. Then we find the LCM of the cycle lengths.
        cycle_lengths = {}
        # Too lazy to fingure out how to reuse start_broadcast, so I'm just copy pasting it.
        button_presses = 0
        while True:
                button_presses += 1
                # changed this from a list to a deque, because the program for som ereason only works with a deque.
                queue = deque([("broadcaster", dest, "low") for dest in self.broadcast])
                
                while queue:
                    origin, target, pulse = queue.popleft()
                    
                    if target not in self.modules:
                        continue
                    
                    module = self.modules[target]
                    
                    if module.name == rx and pulse == "hi":
                        rx_targets[origin] += 1
                        
                        if origin not in cycle_lengths:
                            cycle_lengths[origin] = button_presses

                        if all(rx_targets.values()):
                            return lcm(*cycle_lengths.values())
                            
                    
                    if module.isConjunction:
                        module.state[origin] = pulse
                        outgoing = "low" if all(x == "hi" for x in module.state.values()) else "hi"
                        for x in module.outputs:
                            queue.append((module.name, x, outgoing))
                    else:
                        if pulse == "low":
                            module.state = "on" if module.state == "off" else "off"
                            outgoing = "hi" if module.state == "on" else "low"
                            for x in module.outputs:
                                queue.append((module.name, x, outgoing))