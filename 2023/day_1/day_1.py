input = open("day_1_input.txt", "r")

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

print("answer:", answer)