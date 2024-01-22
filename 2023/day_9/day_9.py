from sys import argv


def every_element_is_zero(numbers) -> bool:
    for element in numbers:
        if element != 0:
            return False
    return True


def get_next_level(numbers) -> list:
    new_list = []
    index = 1

    while index < len(numbers):
        new_list.append(numbers[index] - numbers[index - 1])
        index += 1

    return new_list


def predict_part_one(numbers) -> int:
    lists = []
    lists.append(numbers)
    while True:
        numbers = get_next_level(numbers)
        lists.append(numbers)
        if every_element_is_zero(numbers):
            break

    index = len(lists) - 1
    while index > 0:
        lists[index-1].append(lists[index-1][-1] + lists[index][-1])
        index -= 1

    return lists[0][-1]


def mirage_maintenance_part_one(input) -> int:
    lines = input.readlines()
    answer = 0

    for line in lines:
        numbers = []
        for element in line.split():
            numbers.append(int(element))
        answer += predict_part_one(numbers)

    return answer


def predict_part_two(numbers) -> int:
    lists = []
    lists.append(numbers)
    while True:
        numbers = get_next_level(numbers)
        lists.append(numbers)
        if every_element_is_zero(numbers):
            break

    index = len(lists) - 1
    while index > 0:
        lists[index-1].insert(0, lists[index-1][0] - lists[index][0])
        index -= 1

    return lists[0][0]


def mirage_maintenance_part_two(input) -> int:
    lines = input.readlines()
    answer = 0

    for line in lines:
        numbers = []
        for element in line.split():
            numbers.append(int(element))
        answer += predict_part_two(numbers)

    return answer


def main() -> None:
    if len(argv) > 1:
        if argv[1] == "test":
            input = open("test.txt", "r")
        else:
            input = open("input.txt", "r")
    else:
        input = open("input.txt", "r")

    print("Mirage Maintenance part one answer:",
          mirage_maintenance_part_one(input))
    input.seek(0)
    print("Mirage Maintenance part two answer:",
          mirage_maintenance_part_two(input))


if __name__ == "__main__":
    main()
