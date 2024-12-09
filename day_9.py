example = """2333133121414131402"""

def get_input() -> str:
    with open('day_9_puzzle.txt', 'r') as file:
        content = file.read()
    return content

def parser(data: str) -> [str]:
    expanded = []

    file_id: int = 0
    file_block = True
    for char in data:
        if file_block:
            for i in range(0, int(char)):
                expanded.append(str(file_id))
            file_block = not file_block
            file_id += 1
        else:
            for i in range(0, int(char)):
                expanded += "."
            file_block = not file_block

    return expanded

def part_2(data: str) -> int: # list of tuples, tuple is id, length
    expanded: [(str, int)] = []
    def format(data: [(str, int)]) -> [str]:
        formatted = []
        for symbol_length_pair in expanded:
            for i in range(0, symbol_length_pair[1]):
                formatted.append(str(symbol_length_pair[0]))
        return formatted


    file_id = 0
    free = False
    for char in data:
        if free:
            expanded.append((".", int(char)))
        else:
            expanded.append((str(file_id), int(char)))
            file_id += 1
        free = not free
    #compact files, same algo as before except now we are moving tuples around.

    for i in range(len(expanded)-1, -1, -1):
        # if we would be moving empty space, don't!
        if expanded[i][0] == ".":
            continue

        # at this point the block we want to move is at i, now we need to find some empty space for it:
        target_index = 0
        for j in range(0, len(expanded)):
            if j > i:
                continue
            if expanded[j][0] == "." and expanded[j][1] >= expanded[i][1]:
                extra = expanded[j][1] - expanded[i][1]
                temp = (expanded[j][0], expanded[j][1] - extra) # temp is the block at j (the empty space)

                expanded[j] = (expanded[i][0], expanded[i][1]) # j is the block that was at i (the real block)
                expanded[i] = temp

                expanded.insert(j+1, (".", extra))
                break

    check_sum = calculate_checksum(format(expanded))
    return check_sum



def compact_files(data: [str]) -> [str]:
    front_index = 0
    back_index = len(data) - 1

    # swap data[front] and data [back] when needed, or decide to do nothing and advance:
    while front_index < back_index:
        # if the index we are considering already has data, no need to swap:
        if data[front_index] != ".":
            front_index += 1
            continue
        # if the index we are considering already has data, and backIndex has data, swap them:
        elif data[back_index] != ".":
            data[front_index] = data[back_index]
            data[back_index] = "."

            front_index += 1
            back_index -= 1
            continue

        # if both are ., stay on this index, and move back index only:
        back_index -= 1

    return data

def calculate_checksum(data: [str]) -> int:
    checksum = 0

    for i in range(0, len(data)):
        if data[i] == ".":
            continue
        checksum += i*int(data[i])

    return checksum


print(part_2(example))
print(part_2(get_input()))
