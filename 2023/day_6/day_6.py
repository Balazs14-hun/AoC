from sys import argv
from math import prod


def numbers_from_string_list(list_of_strings) -> list:
    list_of_ints = []
    for string in list_of_strings:
        if string.isdecimal():
            list_of_ints.append(int(string))

    return list_of_ints


def get_strategies(race_time) -> list:
    hold_times = []
    for hold_time in range(int(race_time/2)+1):
        hold_times.append(hold_time*(race_time-hold_time))

    return hold_times


def wait_for_it_part_one(input) -> int:
    lines = input.readlines()
    answers = []
    calculated_times = []

    times = numbers_from_string_list(lines[0].split())
    distances = numbers_from_string_list(lines[1].split())
    for index, time in enumerate(times):
        calculated_times.append(get_strategies(time))

    for index, distance in enumerate(distances):
        if times[index] % 2 != 0:
            answers.append(
                sum(element > distance for element in calculated_times[index]) * 2)
        else:
            answers.append(
                sum(element > distance for element in calculated_times[index]) * 2 - 1)

    return prod(answers)


def digits_from_string_list(list_of_strings) -> list:
    digits = []
    for element in list_of_strings:
        if element.isdecimal():
            for digit in element:
                digits.append(int(digit))

    return digits


def get_int_from_list(digits) -> int:
    number = 0
    place_value = 1

    while len(digits) > 0:
        number += place_value * digits.pop()
        place_value *= 10

    return number


def wait_for_it_part_two(input) -> int:
    lines = input.readlines()

    times = digits_from_string_list(lines[0].split())
    distances = digits_from_string_list(lines[1].split())

    time = get_int_from_list(times)
    distance = get_int_from_list(distances)

    calculated_time = get_strategies(time)

    if time % 2 != 0:
        answer = sum(element > distance for element in calculated_time) * 2
    else:
        answer = sum(element > distance for element in calculated_time) * 2 - 1

    return answer


def main() -> None:
    if len(argv) > 1:
        if argv[1] == "test":
            input = open("test.txt", "r")
        else:
            input = open("input.txt", "r")
    else:
        input = open("input.txt", "r")

    print("Wait For It part one answer:", wait_for_it_part_one(input))
    input.seek(0)
    print("Wait For It part two answer:", wait_for_it_part_two(input))


if __name__ == "__main__":
    main()
