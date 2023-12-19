def get_number_from_string(string):
    digits = []
    for character in string:
        if character.isnumeric():
            digits.append(int(character))

    number = 0
    place_value = 1
    while len(digits) > 0:
        number += place_value * digits.pop()
        place_value *= 10

    return number


def get_first_letter_from_string(string):
    for character in string:
        if character.isalpha():
            return character
    return -1


def flatten_list(list):
    flat_list = []
    for sublist in list:
        flat_list.extend(sublist)
    return flat_list


def cube_conundrum_part_one(input):
    lines = input.readlines()

    answer = 0

    RED_CUBE_LIMIT = 12
    GREEN_CUBE_LIMIT = 13
    BLUE_CUBE_LIMIT = 14

    for line in lines:
        game = line.split(": ")
        id = get_number_from_string(game[0])
        records = game[1].split("; ")
        for index, record in enumerate(records):
            records[index] = record.split(", ")
        records = flatten_list(records)

        game_is_possible = True
        for record in records:
            number_of_cubes = get_number_from_string(record)
            match get_first_letter_from_string(record):
                case "r":
                    if number_of_cubes > RED_CUBE_LIMIT:
                        game_is_possible = False
                        break
                case "g":
                    if number_of_cubes > GREEN_CUBE_LIMIT:
                        game_is_possible = False
                        break
                case "b":
                    if number_of_cubes > BLUE_CUBE_LIMIT:
                        game_is_possible = False
                        break
                case _:
                    continue

        if game_is_possible:
            answer += id

    return answer


def cube_conundrum_part_two(input):
    lines = input.readlines()

    answer = 0

    for line in lines:
        minimum_of_red_cubes = 0
        minimum_of_green_cubes = 0
        minimum_of_blue_cubes = 0

        game = line.split(": ")
        records = game[1].split("; ")
        for index, record in enumerate(records):
            records[index] = record.split(", ")
        records = flatten_list(records)

        for record in records:
            number_of_cubes = get_number_from_string(record)
            match get_first_letter_from_string(record):
                case "r":
                    if number_of_cubes > minimum_of_red_cubes:
                        minimum_of_red_cubes = number_of_cubes
                case "g":
                    if number_of_cubes > minimum_of_green_cubes:
                        minimum_of_green_cubes = number_of_cubes
                case "b":
                    if number_of_cubes > minimum_of_blue_cubes:
                        minimum_of_blue_cubes = number_of_cubes
                case _:
                    continue

        answer += minimum_of_red_cubes * \
            minimum_of_green_cubes * \
            minimum_of_blue_cubes

    return answer


def main():
    input = open("day_2_input.txt", "r")

    print("Cube Conundrum part one answer: ", cube_conundrum_part_one(input))
    input.seek(0)
    print("Cube Conundrum part two answer: ", cube_conundrum_part_two(input))


if __name__ == "__main__":
    main()
