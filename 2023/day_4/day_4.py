def string_to_numbers(string):
    digits = []
    numbers = []

    for character in string:
        if character.isdecimal():
            digits.append(int(character))
        else:
            if len(digits) > 0:
                number = 0
                place_value = 1
                while len(digits) > 0:
                    number += place_value * digits.pop()
                    place_value *= 10

                numbers.append(number)

    return numbers


def scratchcards_part_one(input):
    lines = input.readlines()

    answer = 0

    for line in lines:
        points = 0

        card = line.split(":")
        numbers_on_card = card[1].split("|")
        winning_numbers = string_to_numbers(numbers_on_card[0])
        numbers_you_have = set(string_to_numbers(numbers_on_card[1]))
        for number in winning_numbers:
            if number in numbers_you_have:
                if points == 0:
                    points += 1
                else:
                    points *= 2

        answer += points

    return answer


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


def scratchcards_part_two(input):
    lines = input.readlines()

    card_copies = [1]*len(lines)

    for line in lines:
        points = 0

        card = line.split(":")
        card_number = get_number_from_string(card[0])-1
        numbers_on_card = card[1].split("|")
        winning_numbers = string_to_numbers(numbers_on_card[0])
        numbers_you_have = set(string_to_numbers(numbers_on_card[1]))
        for number in winning_numbers:
            if number in numbers_you_have:
                points += 1

        win_index = card_number+1
        while points > 0:
            card_copies[win_index] += card_copies[card_number]
            win_index += 1
            points -= 1

    answer = sum(card_copies)

    return answer


def main():
    input = open("day_4_input.txt", "r")

    print("Scratchcards part one answer: ", scratchcards_part_one(input))
    input.seek(0)
    print("Scratchcards part two answer: ", scratchcards_part_two(input))


if __name__ == "__main__":
    main()
