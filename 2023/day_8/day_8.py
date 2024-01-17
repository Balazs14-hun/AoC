from sys import argv
from math import lcm


class Rule:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return self.left + " - " + self.right


def count_steps_part_one(instructions, rules) -> int:
    next_step = "AAA"
    counter = 0
    instruction_index = 0

    while next_step != "ZZZ":
        if instructions[instruction_index] == "L":
            next_step = rules[next_step].left
        else:
            next_step = rules[next_step].right

        instruction_index += 1
        if instruction_index >= len(instructions):
            instruction_index = 0
        counter += 1

    return counter


def haunted_wasteland_part_one(input) -> int:
    lines = input.readlines()
    rules = {}

    for line in lines:
        line = line.split()
        if len(line) == 1:
            instructions = line[0]
        elif len(line) > 1:
            left = line[2][1] + line[2][2] + line[2][3]
            right = line[3][0] + line[3][1] + line[3][2]
            rules.update({line[0]: Rule(left, right)})

    answer = count_steps_part_one(instructions, rules)

    return answer


def count_steps_part_two(instructions, rules) -> int:
    next_steps = []
    for rule in rules:
        if rule[2] == "A":
            next_steps.append([rule, 0])

    counter = 0
    instruction_index = 0
    repeat_lenghts = [0]*len(next_steps)

    while True:
        if instructions[instruction_index] == "L":
            for index, next_step in enumerate(next_steps):
                next_steps[index] = [
                    rules[next_step[0]].left, next_step[1] + 1]
                if next_step[0][2] == "Z":
                    repeat_lenghts[index] = next_step[1]
                    next_steps[index][1] = 0

        else:
            for index, next_step in enumerate(next_steps):
                next_steps[index] = [
                    rules[next_step[0]].right, next_step[1] + 1]
                if next_step[0][2] == "Z":
                    repeat_lenghts[index] = next_step[1]
                    next_steps[index][1] = 0

        for repeat_lenght in repeat_lenghts:
            stop = True
            if repeat_lenght == 0:
                stop = False

        if stop:
            break

        instruction_index += 1
        if instruction_index >= len(instructions):
            instruction_index = 0
        counter += 1

    return lcm(*repeat_lenghts)


def haunted_wasteland_part_two(input) -> int:
    lines = input.readlines()
    rules = {}

    for line in lines:
        line = line.split()
        if len(line) == 1:
            instructions = line[0]
        elif len(line) > 1:
            left = line[2][1] + line[2][2] + line[2][3]
            right = line[3][0] + line[3][1] + line[3][2]
            rules.update({line[0]: Rule(left, right)})

    answer = count_steps_part_two(instructions, rules)

    return answer


def main() -> None:
    if len(argv) > 1:
        if argv[1] == "test":
            input1 = open("test1.txt", "r")
            input2 = open("test2.txt", "r")
        else:
            input1 = open("input.txt", "r")
            input2 = open("input.txt", "r")
    else:
        input1 = open("input.txt", "r")
        input2 = open("input.txt", "r")

    print("Haunted Wasteland part one answer:",
          haunted_wasteland_part_one(input1))
    print("Haunted Wasteland part two answer:",
          haunted_wasteland_part_two(input2))


if __name__ == "__main__":
    main()
