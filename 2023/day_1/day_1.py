def part_one(input):
    lines = input.readlines()

    answer = 0

    for line in lines:
        first_digit = -1
        last_digit = -1
        for character in line:
            if character.isnumeric():
                if first_digit == -1:
                    first_digit = character
                else:
                    last_digit = character
        if last_digit == -1:
            last_digit = first_digit
        calibration_value = 10*int(first_digit) + int(last_digit)
        answer += calibration_value

    return answer


def part_two(input):
    search_words = ["one", "two", "three", "four",
                    "five", "six", "seven", "eight", "nine"]

    lines = input.readlines()

    answer = 0

    for line in lines:
        line_length = len(line)
        first_digits = [line_length, line_length, line_length, line_length,
                        line_length, line_length, line_length, line_length, line_length]
        last_digits = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

        # numeric digits ------------------------------------------------------
        first_digit = -1
        first_digit_index = -1
        last_digit = -1
        last_digit_index = -1

        for index, character in enumerate(line):
            if character.isnumeric():
                if first_digit == -1:
                    first_digit = character
                    first_digit_index = index
                else:
                    last_digit = character
                    last_digit_index = index
        if last_digit == -1:
            last_digit = first_digit
            last_digit_index = first_digit_index

        first_digits[int(first_digit)-1] = first_digit_index
        last_digits[int(last_digit)-1] = last_digit_index
        # ---------------------------------------------------------------------

        # written digits ------------------------------------------------------
        for index, word in enumerate(search_words):
            small_occurance_index = line.find(word)
            big_occurance_index = line.rfind(word)
            if small_occurance_index != -1:
                if small_occurance_index < first_digits[index]:
                    first_digits[index] = small_occurance_index
            if big_occurance_index != -1:
                if big_occurance_index > last_digits[index]:
                    last_digits[index] = big_occurance_index
        # ---------------------------------------------------------------------

        found_first_digit = first_digits.index(min(first_digits)) + 1
        found_last_digit = last_digits.index(max(last_digits)) + 1

        calibration_value = 10*found_first_digit + found_last_digit
        answer += calibration_value

    return answer


def main():
    input = open("day_1_input.txt", "r")

    print("Part one answer: ", part_one(input))
    input.seek(0)
    print("Part two answer: ", part_two(input))


if __name__ == "__main__":
    main()
