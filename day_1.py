example = """
3 4
4 3
2 5
1 3
3 9
3 3
"""

def parse_input(input_string: str) -> ([int], [int]):
    numbers = [int(num) for num in input_string.split()]
    left = numbers[::2]
    right = numbers[1::2]
    left.sort()
    right.sort()
    return left, right

def calculate_difference(input_string: str) -> int:
    to_return = 0
    left, right = parse_input(input_string)
    for left, right in zip(left, right):
        to_return += abs(left - right)
    return to_return

def calculate_similarly(input_string: str) -> int:
    to_return = 0
    left, right = parse_input(input_string)
    for number in left:
        to_add = right.count(number)*number
        to_return += to_add
    return to_return

def get_input() -> str:
    with open('day_1_puzzle.txt', 'r') as file:
        content = file.read()
    return content

print(calculate_difference(example))
print(calculate_similarly(example))
print(calculate_difference(get_input()))
print(calculate_similarly(get_input()))