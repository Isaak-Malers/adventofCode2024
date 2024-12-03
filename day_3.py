import re

example = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

example_2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


def get_input() -> str:
    with open('day_3_puzzle.txt', 'r') as file:
        content = file.read()
    return content

def extract_mul_matches(input_string: str) -> [str]:
    # Define the regular expression pattern
    pattern = r"mul\([0-9]*,[0-9]*\)"

    # Use re.findall() to find all non-overlapping matches
    matches = re.findall(pattern, input_string)

    return matches

def extract_either(input_string: str) -> [str]:
    # Define the regular expression pattern
    pattern = r"(mul\([0-9]*,[0-9]*\))|(do\(\))|(don't\(\))"

    # Use re.findall() to find all non-overlapping matches
    matches = re.findall(pattern, input_string)

    re_formated = []
    for match in matches:
        for sub_match in match:
            if len(sub_match) != 0:
                re_formated.append(sub_match)
                continue

    return re_formated


def parse_instruction(input_string) -> (int, int):
    # Remove the 'mul(' prefix and the closing ')' parenthesis
    input_string = input_string[len("mul("):-1]

    # Split the string by the comma
    number_a_str, number_b_str = input_string.split(',')

    # Strip any whitespace and convert to integers
    number_a = int(number_a_str.strip())
    number_b = int(number_b_str.strip())

    return number_a, number_b

def do_math(input_string: str) -> int:
    total = 0
    values = extract_mul_matches(input_string)
    for operation in values:
        a, b = parse_instruction(operation)
        total += a*b
    return total

def do_math_with_extras(input_string: str) -> int:
    total = 0
    values = extract_either(input_string)
    do_adds = True
    for operation in values:
        if operation == "don't()":
            do_adds = False
        elif operation == "do()":
            do_adds = True
        elif do_adds:
            a, b = parse_instruction(operation)
            total += a*b
    return total

print(do_math(example))
print(do_math_with_extras(example_2))
print(do_math(get_input()))
print(do_math_with_extras(get_input()))