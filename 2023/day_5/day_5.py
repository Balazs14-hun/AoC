class map:
    def __init__(self, source_name, destination_name) -> None:
        self.source_name = source_name
        self.destination_name = destination_name
        self.source_starts = []
        self.destinations_starts = []
        self.ranges = []

    def add_rule(self, destionation, source, range) -> None:
        self.source_starts.append(source)
        self.destinations_starts.append(destionation)
        self.ranges.append(range)

    def get_destination_from_source(self, source):
        destination = source
        for index, source_start in enumerate(self.source_starts):
            if source_start <= source <= source_start + self.ranges[index]:
                destination = self.destinations_starts[index] + (
                    source-source_start)
                return destination
        return destination

    def __str__(self) -> str:
        return self.source_name + " -> " + self.destination_name


def string_to_int(list_of_strings) -> list:
    list_of_ints = []
    for string in list_of_strings:
        list_of_ints.append(int(string))

    return list_of_ints


# it works when the words are separated by spaces
def first_word_from_string(string) -> str:
    words = string.split()

    return words[0]


def give_a_seed_a_fertilizer_part_one(input) -> int:
    lines = input.readlines()
    maps = []
    answers = []

    for line in lines:
        entry = line.split(":")
        token = entry[0].split("-")

        if token[0] == "seeds":
            seeds = string_to_int(entry[1].split())
        elif len(token) >= 3:
            maps.append(map(token[0], first_word_from_string(token[2])))
        else:
            if len(entry[0]) > 1:
                rule = string_to_int(entry[0].split())
                maps[-1].add_rule(rule[0], rule[1], rule[2])

    for seed in seeds:
        answer = seed
        for my_map in maps:
            answer = my_map.get_destination_from_source(answer)
        answers.append(answer)

    return min(answers)


def give_a_seed_a_fertilizer_part_two(input) -> int:
    pass

def main() -> None:
    input = open("day_5_input.txt", "r")

    print("Give A Seed A Fertilizer part one answer:",
          give_a_seed_a_fertilizer_part_one(input))
    input.seek(0)
    print("Give A Seed A Fertilizer part two answer:",
          give_a_seed_a_fertilizer_part_two(input))


if __name__ == "__main__":
    main()
