import copy

example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

def parse_input(input_string: str) -> [[str]]:
    to_return = []
    rows = input_string.splitlines()
    for row in rows:
        to_return.append(list(row))
    return to_return


def walk(map: [[str]]) -> ([[str]], str):
    # find the guard, if not specified:
    guard_row = None
    guard_column = None
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] in ["^", "v", "<", ">"]:
                guard_row = i
                guard_column = j

    # run one step:

    def find_next_spot() -> (int, int):
        current = map[guard_row][guard_column]
        if current == "^":
            return guard_row - 1, guard_column
        if current == "v":
            return guard_row + 1, guard_column
        if current == "<":
            return guard_row, guard_column - 1
        if current == ">":
            return guard_row, guard_column +1

    def rotated_dude() -> str:
        current = map[guard_row][guard_column]
        if current == "^":
            return ">"
        if current == "v":
            return "<"
        if current == "<":
            return "^"
        if current == ">":
            return "v"

    steps_since_las_new = 0
    grid_size = len(map) * len(map[0])
    while True:
        row, column = find_next_spot()

        if row < 0 or row >= len(map):
            map[guard_row][guard_column] = "X"
            break
        if column < 0 or column >= len(map):
            map[guard_row][guard_column] = "X"
            break

        if map[row][column] == ".":
            steps_since_las_new = 0
        else:
            steps_since_las_new += 1
            if steps_since_las_new > grid_size:
                return map, "looping"

        # if the new spot is un-occupied, or is just something that's already been visited, move into it.
        if map[row][column] in [".", "X"]:
            map[row][column] = map[guard_row][guard_column]
            map[guard_row][guard_column] = "X"
            guard_row = row
            guard_column = column
            continue

        # if the spot is occupied, replace the
        if map[row][column] in ["#"]:
            map[guard_row][guard_column] = rotated_dude()
            continue

    return map, "exited"

def count_spaces(input_string: str) -> int:
    mapped = parse_input(input_string)
    simulated, exited = walk(mapped)
    count_x = sum(rows.count('X') for rows in simulated)
    return count_x

def count_spots_that_cause_loop(input_string: str) -> int:
    mapped = parse_input(input_string)

    potential_blocks = 0
    for row in range(0, len(mapped)):
        print(f"simulating row: {row} of {len(mapped)}")
        for col in range(0, len(mapped[row])):
            temp = copy.deepcopy(mapped)
            if temp[row][col] in ["."]:
                temp[row][col] = "#"
                simulated, exited = walk(temp)
                if exited == "looping":
                    potential_blocks += 1

    return potential_blocks


def get_input() -> str:
    with open('day_6_puzzle.txt', 'r') as file:
        content = file.read()
    return content

print(count_spaces(example))
print(count_spaces(get_input()))
print()
print(count_spots_that_cause_loop(example))
print(count_spots_that_cause_loop(get_input()))