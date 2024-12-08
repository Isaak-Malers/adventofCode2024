import math
from itertools import combinations
from os import times_result

example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def get_input() -> str:
    with open('day_8_puzzle.txt', 'r') as file:
        content = file.read()
    return content

def parse_input(data: str) -> [[str]]:
    rows = data.splitlines()
    return [[char for char in row] for row in rows]


def solve_puzzle(data: str, resonate: bool = False) -> int:
    uniques = list(set(data) - set([".", "\n"]))
    puzzle_map = parse_input(data)

    sets_of_nodes = {}
    for freq in uniques:
        sets_of_nodes[freq] = []

    for row in range(0, len(puzzle_map)):
        for column in range(0, len(puzzle_map[row])):
            if puzzle_map[row][column] in uniques:
                sets_of_nodes[puzzle_map[row][column]].append([row, column])

    anti_nodes = set()
    for key, value in sets_of_nodes.items():
        for pair in combinations(value, 2):
            new_antinodes = calculate_anti_nodes(pair[0], pair[1], resonate, len(puzzle_map))
            for anti_node in new_antinodes:
                anti_nodes.add((anti_node[0], anti_node[1]))

    anti_nodes_on_map = []
    for node in anti_nodes:
        if node[0] < 0 or node[0] >= len(puzzle_map):
            continue
        if node[1] < 0 or node[1] >= len(puzzle_map[0]):
            continue
        anti_nodes_on_map.append(node)
        #print(f"anti-node: {node[0]},{node[1]}")

    for node in anti_nodes_on_map:
        if puzzle_map[node[0]][node[1]] == ".":
            puzzle_map[node[0]][node[1]] = "#"

    for row in puzzle_map:
        print("".join(row))

    return len(anti_nodes_on_map)


def calculate_anti_nodes(a: [int], b: [int], resonate: bool = False, coord_limit: int = 50) -> [[int]]:
    # this gets much simpler if we think of a, b as vectors from the origin to the point.
    # we can subtract them to get the vector from a to b.
    # then we can do b + b_relative_to_a
    # and a - 180deg flipped b_relative_to_a
    b_relative_to_a  = [b[0]-a[0], b[1]-a[1]]
    b_relative_to_a_flipped = [-b_relative_to_a[0], -b_relative_to_a[1]]

    # directionB:
    to_return = [b]
    while True:
        new_node = [to_return[-1][0] + b_relative_to_a[0], to_return[-1][1] + b_relative_to_a[1]]
        if new_node[0] < 0 or new_node[0] > coord_limit or new_node[1] < 0 or new_node[1] > coord_limit:
            break
        to_return.append(new_node)
        if not resonate:
            break

    # directionA:
    to_return.append(a)
    while True:
        new_node = [to_return[-1][0] + b_relative_to_a_flipped[0], to_return[-1][1] + b_relative_to_a_flipped[1]]
        if new_node[0] < 0 or new_node[1] > coord_limit:
            break
        to_return.append(new_node)
        if not resonate:
            break

    return to_return


#print(solve_puzzle(example))
#print(solve_puzzle(get_input()))

print(solve_puzzle(example, True))
print(solve_puzzle(get_input(), True))