example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

example2 = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""

example_3 = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""

directions = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"]

def get_input() -> str:
    with open('day_4_puzzle.txt', 'r') as file:
        content = file.read()
    return content

def parse_input(input_string: str) -> [[str]]:
    lines = input_string.splitlines()
    to_return = []
    for line in lines:
        to_return.append(list(line))
    return to_return

def generate_string_from_coord(row: int, col: int, grid: [[str]], direction: str, output_length: int) -> str:
    if direction not in directions:
        raise ValueError(f"direction must be in: {directions}")

    if row < 0 or row > len(grid):
        return ""

    if col < 0 or col > len(grid[row]):
        return ""

    result = []

    for i in range(0, output_length):
        try:
            result.append(grid[row][col])

            if "north" in direction:
                row -= 1
            if "south" in direction:
                row += 1
            if "west" in direction:
                col -= 1
            if "east" in direction:
                col += 1

            if col < 0 or row < 0:
                break

            if row > len(grid) or col > len(grid[row]):
                break

        except IndexError:
            return ""

    return "".join(result)


def calculate_xmas_count(input_string: str) -> int:
    values = parse_input(input_string)
    count = 0

    for row in range(0, len(values)):
        for col in range(0, len(values[row])):
            letter = values[row][col]

            # we need to find XMAS in here:
            if letter != "X":
                continue
            for direction in directions:
                maybe_xmas = generate_string_from_coord(row, col, values, direction, 4)
                if maybe_xmas == "XMAS":
                    count += 1
    return count

def calculate_mas_x_count(input_string: str) -> int:
    values = parse_input(input_string)
    count = 0

    for row in range(0, len(values)):
        for col in range(0, len(values[row])):
            letter = values[row][col]

            # we need to find MAS in here:
            if letter != "A":
                continue
            # we are on an "a".

            #check diagonal northwest of the a
            north_west_row = row-1
            north_west_column = col-1
            maybe_mas_or_sas = generate_string_from_coord(north_west_row, north_west_column, values, "southeast", 3)
            if not (maybe_mas_or_sas == "MAS" or maybe_mas_or_sas == "SAM"):
                continue

            #check diagonal northeast of the a
            north_east_row = row-1
            north_east_column = col+1
            maybe_mas_or_sas = generate_string_from_coord(north_east_row, north_east_column, values, "southwest", 3)
            if not (maybe_mas_or_sas == "MAS" or maybe_mas_or_sas == "SAM"):
                continue
            count += 1

    return count

print(calculate_xmas_count(example))
print(calculate_xmas_count(example2))
print(calculate_xmas_count(get_input()))
print(calculate_mas_x_count(example_3))
print(calculate_mas_x_count(get_input()))