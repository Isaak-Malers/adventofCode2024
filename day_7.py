import itertools
from asyncio import to_thread

example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


operators = ["+", "*"]

def get_input() -> str:
    with open('day_7_puzzle.txt', 'r') as file:
        content = file.read()
    return content

def generate_permutations(ops: [str], n: int) -> [[str]]:
    # Generate all permutations of length n
    return [list(perm) for perm in itertools.product(ops, repeat=n)]

def parse_input(data: str) -> [int, [int]]:
    rows = data.splitlines()
    to_return = []
    for row in rows:
        to_return.append((int(row.split(":")[0]), [int(x) for x in row.split(":")[1].strip().split(" ")]))
    return to_return


def do_math(nums: [int], ops: [str]) -> int:
    to_return = int(nums[0])

    for i in range(0, len(nums)-1):
        if ops[i] == "+":
            to_return = to_return + int(nums[i+1])
        if ops[i] == "*":
            to_return = to_return * int(nums[i+1])
        if ops[i] == "||":
            to_return = int(str(to_return) + str(nums[i+1]))

    return to_return

def find_operators(goal: int, contributors: [int]) -> [str]:
    all_ops = generate_permutations(operators, len(contributors)-1)
    for ops in all_ops:
        result = do_math(contributors, ops)
        if goal == result:
            return ops
    return None

def find_answer(data: str) -> int:
    to_search = parse_input(data)
    to_return = 0

    for line in to_search:
        ops = find_operators(line[0], line[1])
        if ops is None:
            continue
        to_return += do_math(line[1], ops)

    return to_return

print("part1")
print(find_answer(example))
print(find_answer(get_input()))
operators.append("||")
print("part2")
print(find_answer(example))
print(find_answer(get_input()))