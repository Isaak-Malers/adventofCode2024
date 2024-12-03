example = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

# ensure all increasing or all decreasing
# adjacent numbers differ by 1 at minimum and 3 at maximum

def get_input() -> str:
    with open('day_2_puzzle.txt', 'r') as file:
        content = file.read()
    return content

def parse_input(input_str: str) -> [[int]]:
    to_return = []
    lines = input_str.splitlines()
    for line in lines:
        numbers = list(map(int, line.split()))
        if len(numbers) == 0:
            continue
        to_return.append(numbers)
    return to_return

def calculate_safe_reports(input_str: str) -> int:
    def is_between(x, a, b):
        return a <= x <= b or b <= x <= a

    reports = parse_input(input_str)
    safe = 0
    for report in reports:
        direction = 1
        if report[0] > report[1]:
            direction = -1

        report_safe = True
        for a, b in zip(report, report[1:]):
            min_deviated = a + direction
            max_deviated = a + 3*direction
            if not is_between(b, min_deviated, max_deviated):
                report_safe = False
                break

        if report_safe:
            safe += 1

    return safe

def calculate_safe_report_with_damper(report: [int], recurse=True) -> bool:
    def is_between(x, a, b):
        return a <= x <= b or b <= x <= a

    direction = 1
    if report[0] > report[1]:
        direction = -1

    report_safe = True
    for a, b in zip(report, report[1:]):
        min_deviated = a + direction
        max_deviated = a + 3 * direction
        if not is_between(b, min_deviated, max_deviated):
            report_safe = False
            break

    # If it's safe without the damper, it will be WITH the damper
    if report_safe:
        return True

    # If it is not safe without the damper, try removing values and if it is safe, return True
    if recurse:
        for i in range(0, len(report)):
            potential = report[:i] + report[i+1:]
            if calculate_safe_report_with_damper(potential, False):
                return True

    return False

def calculate_safe_reports_with_damper(input_str: str) -> int:


    reports = parse_input(input_str)
    safe = 0
    for report in reports:
        report_safe = calculate_safe_report_with_damper(report)
        if report_safe:
            safe += 1

    return safe

print(calculate_safe_reports(example))
print(calculate_safe_reports_with_damper(example))
print(calculate_safe_reports(get_input()))
print(calculate_safe_reports_with_damper(get_input()))