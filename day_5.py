example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


class Input:
    def __init__(self):
        self.rules: [[int]] = []
        self.updates: [[int]] = []

def get_input() -> str:
    with open('day_5_puzzle.txt', 'r') as file:
        content = file.read()
    return content

def parse_input(input_string: str) -> Input:
    to_return = Input()

    rules_str = input_string.split("\n\n")[0]
    updates_str = input_string.split("\n\n")[1]
    for rule_str in rules_str.splitlines():
        to_return.rules.append(list(map(int, rule_str.split("|"))))
    for update_str in updates_str.splitlines():
        to_return.updates.append(list(map(int, update_str.split(","))))

    return to_return

def calculate_middle_pages_of_correct(input_str: str) -> int:
    data = parse_input(input_str)
    total_of_middles = 0
    for update in data.updates:

        #print(update)
        valid = True
        # first find out if the update is valid:
        for rule in data.rules:
            if rule[0] in update and rule[1] in update: # rule applies to this update
                first = update.index(rule[0])
                second = update.index(rule[1])
                if first > second:
                    #print(f"\tInvalid Update: rule: {rule[0]}|{rule[1]} : update: {update}")
                    valid = False
                    break

        if valid:
            total_of_middles += update[int(len(update)/2)]

    return total_of_middles


def calculate_middle_pages_of_corrected(input_str: str) -> int:
    data = parse_input(input_str)
    total_of_middles_correct = 0
    total_of_middles_corrected = 0

    for update in data.updates:

        #print(update)
        valid = True
        # first find out if the update is valid:
        for rule in data.rules:
            if rule[0] in update and rule[1] in update: # rule applies to this update
                first = update.index(rule[0])
                second = update.index(rule[1])
                if first > second:
                    print(f"\tInvalid Update: rule: {rule[0]}|{rule[1]} : update: {update}")
                    valid = False
                    #now let's correct this, and add its middle to the corrected total:

        if not valid:
            corrected = correct_update(data.rules, update)
            print(f"corrected: {corrected}")
            total_of_middles_corrected += corrected[int(len(corrected)/2)]

        if valid:
            total_of_middles_correct += update[int(len(update)/2)]

    return total_of_middles_corrected

def rules_to_update(rules: [[int]]) -> [int]:
    if len(rules) == 0:
        return []

    all_lefts = set()
    all_rights = set()

    for rule in rules:
        all_lefts.add(rule[0])
        all_rights.add(rule[1])

    only_left = (all_lefts - all_rights).pop()

    # remove the only left rule from rules, and recurse:
    smaller_rules_set = []
    for rule in rules:
        if rule[0] != only_left:
            smaller_rules_set.append(rule)

    the_rest = rules_to_update(smaller_rules_set)
    the_rest.insert(0, only_left)

    unique_lst = []
    seen = set()

    for item in the_rest:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)

    return unique_lst



def correct_update(rules: [[int]], to_correct: [int]) -> [int]:
    applicable_rules = []

    for rule in rules:
        if rule[0] in to_correct and rule[1] in to_correct:
            applicable_rules.append(rule)

    return rules_to_update(applicable_rules)


print(calculate_middle_pages_of_correct(example))
print(calculate_middle_pages_of_correct(get_input()))
print(calculate_middle_pages_of_corrected(example))
print(calculate_middle_pages_of_corrected(get_input()))