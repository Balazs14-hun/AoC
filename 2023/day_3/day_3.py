def is_symbol(character):
    if character.isdecimal():
        return False
    elif character == ".":
        return False
    else:
        return True


def is_star(character):
    if character == "*":
        return True
    return False


def gear_ratios_part_one(input):
    lines = (input.readlines())
    line_length = len(lines[0])

    lines.insert(0, "."*(line_length-1))
    lines.append("."*(line_length-1))

    answer = 0

    index = 1
    while index < len(lines)-1:
        lines[index] = lines[index] + "."
        is_part_number = False
        digits = []

        for character_index, character in enumerate(lines[index]):
            if character.isdecimal():
                digits.append(int(character))
                if not is_part_number:
                    if character_index != 0:
                        if is_symbol(lines[index-1][character_index-1]):
                            is_part_number = True
                            continue
                        if is_symbol(lines[index][character_index-1]):
                            is_part_number = True
                            continue
                        if is_symbol(lines[index+1][character_index-1]):
                            is_part_number = True
                            continue
                    if is_symbol(lines[index-1][character_index]):
                        is_part_number = True
                        continue
                    if is_symbol(lines[index+1][character_index]):
                        is_part_number = True
                        continue
                    if character_index < line_length-2:
                        if is_symbol(lines[index-1][character_index+1]):
                            is_part_number = True
                            continue
                        if is_symbol(lines[index][character_index+1]):
                            is_part_number = True
                            continue
                        if is_symbol(lines[index+1][character_index+1]):
                            is_part_number = True
                            continue
                continue

            if is_part_number:
                part_number = 0
                place_value = 1
                while len(digits) > 0:
                    part_number += place_value * digits.pop()
                    place_value *= 10

                is_part_number = False

                answer += part_number
            else:
                digits = []

        index += 1

    return answer


def get_connected_digits(line, start_index, visited, visited_index, visited_line):
    digits = []
    asc_index = start_index
    desc_index = start_index-1
    visited_index_tmp = visited_index
    while asc_index < len(line) and line[asc_index].isdecimal():
        digits.append(int(line[asc_index]))
        if visited_index_tmp >= 0 and visited_index_tmp < 3:
            visited[visited_line][visited_index_tmp] = True
            visited_index_tmp += 1
        asc_index += 1

    visited_index_tmp = visited_index - 1
    while desc_index < len(line) and line[desc_index].isdecimal():
        digits.insert(0, int(line[desc_index]))
        if visited_index_tmp >= 0 and visited_index_tmp < 3:
            visited[visited_line][visited_index_tmp] = True
            visited_index_tmp -= 1
        desc_index -= 1

    return visited, digits


def number_from_list(list_of_digits):
    number = 0
    place_value = 1
    while len(list_of_digits) > 0:
        number += place_value * list_of_digits.pop()
        place_value *= 10
    return number


def gear_ratios_part_two(input):
    lines = (input.readlines())
    line_length = len(lines[0])

    lines.insert(0, "."*(line_length-1))
    lines.append("."*(line_length-1))

    answer = 0

    index = 1
    while index < len(lines)-1:
        lines[index] = lines[index] + "."

        for character_index, character in enumerate(lines[index]):
            if is_star(character):
                part_numbers = []
                visited = [[False, False, False],
                           [False, True, False],
                           [False, False, False]]

                if not visited[0][0] and lines[index-1][character_index-1].isdecimal():
                    visited, digits = get_connected_digits(
                        lines[index-1], character_index-1, visited, 0, 0)
                    part_numbers.append(number_from_list(digits))
                if not visited[0][1] and lines[index-1][character_index].isdecimal():
                    visited, digits = get_connected_digits(
                        lines[index-1], character_index, visited, 1, 0)
                    part_numbers.append(number_from_list(digits))
                if not visited[0][2] and lines[index-1][character_index+1].isdecimal():
                    visited, digits = get_connected_digits(
                        lines[index-1], character_index+1, visited, 2, 0)
                    part_numbers.append(number_from_list(digits))
                if not visited[1][0] and lines[index][character_index-1].isdecimal():
                    visited, digits = get_connected_digits(
                        lines[index], character_index-1, visited, 0, 1)
                    part_numbers.append(number_from_list(digits))
                if not visited[1][2] and lines[index][character_index+1].isdecimal():
                    visited, digits = get_connected_digits(
                        lines[index], character_index+1, visited, 2, 1)
                    part_numbers.append(number_from_list(digits))
                if not visited[2][0] and lines[index+1][character_index-1].isdecimal():
                    visited, digits = get_connected_digits(
                        lines[index+1], character_index-1, visited, 0, 2)
                    part_numbers.append(number_from_list(digits))
                if not visited[2][1] and lines[index+1][character_index].isdecimal():
                    visited, digits = get_connected_digits(
                        lines[index+1], character_index, visited, 1, 2)
                    part_numbers.append(number_from_list(digits))
                if not visited[2][2] and lines[index+1][character_index+1].isdecimal():
                    visited, digits = get_connected_digits(
                        lines[index+1], character_index+1, visited, 2, 2)
                    part_numbers.append(number_from_list(digits))

                if len(part_numbers) == 2:
                    first_number = part_numbers.pop()
                    second_number = part_numbers.pop()
                    answer = answer + (first_number * second_number)

        index += 1

    return answer


def main():
    input = open("day_3_input.txt", "r")

    print("Gear Ratios part one answer: ", gear_ratios_part_one(input))
    input.seek(0)
    print("Gear Ratios part two answer: ", gear_ratios_part_two(input))


if __name__ == "__main__":
    main()
