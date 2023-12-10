import re

# FML graph theory =(
def part1(grid):
    seen = set()
    start = [(y, x) for y, row in enumerate(grid) for x, col in enumerate(row) if col == "S"][0]
    seen.add(start)
    queue = [start]
    
    # doing BFS
    while queue: 
        row, col = queue.pop()
        char = grid[row][col]
        
        # Can go north/ accepts from south
        if row > 0  and char in "S|JL" and grid[row-1][col] in "|7F" and (row-1, col) not in seen:
            queue.append((row-1, col))
            seen.add((row-1, col))
        # Can go south / accepts from north
        if row < len(grid)-1 and char in "S|7F" and grid[row+1][col] in "|JL" and (row+1, col) not in seen:
            queue.append((row+1, col))
            seen.add((row+1, col))
        # Can go weast / accepts from east
        if col > 0 and char in "S-J7" and grid[row][col-1] in "-LF" and (row, col-1) not in seen:
            queue.append((row, col-1))
            seen.add((row, col-1))
        # Can go east / accepts from weast
        if col < len(grid [row])-1 and char in "S-LF" and grid[row][col+1] in "-J7" and (row, col+1) not in seen:
            queue.append((row, col+1))
            seen.add((row, col+1))
            
    return start, seen

# This is a mess, but it works
def replace_S(start, seen):
    if (start[0]-1, start[1]) in seen: # north
        if (start[0]+1, start[1]) in seen: # south
            return "|"
            
        elif (start[0], start[1]-1) in seen: # weast
            return "J"
            
        elif (start[0], start[1]+1) in seen: # east
            return "L"
            
    elif (start[0]+1, start[1]) in seen: # south
        if (start[0], start[1]-1) in seen:     
            return "7" # west
        elif (start[0], start[1]+1) in seen: # east
            return "F"
    else:
        return "-"
        
def part2(grid):
    start, loop = part1(grid)
    grid= [row.replace("S", replace_S(start, loop)) for row in grid]
  
    for y, row in enumerate(grid):
        grid[y] = "".join([col if (y, x) in loop else "." for x, col in enumerate(row)])

    inside = 0
    for y, row in enumerate(grid):
        row = re.sub(r"L-*J|F-*7", "", row)
        within = False
        for _, col in enumerate(row):
            if col in "|FL":
                within = not within
            if within and col == ".":
                inside += 1
    return inside

def main():
    input = open("input.txt", "r").read().splitlines()
    _, part1_sum = part1(input)
    part2_sum = part2(input)
    print(f"Part 1: {len(part1_sum) // 2}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()