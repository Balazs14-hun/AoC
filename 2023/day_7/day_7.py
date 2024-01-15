from sys import argv


class Hand:
    def __init__(self, entry) -> None:
        self.cards = entry[0]
        self.bid = int(entry[1])
        self.strengths = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9,
                          "9": 8, "8": 7, "7": 6, "6": 5, "5": 4,
                          "4": 3, "3": 2, "2": 1}

        tmp = {}

        for card in self.cards:
            if card in tmp:
                tmp[card] += 1
            else:
                tmp.update({card: 1})

        match len(tmp):
            case 1:
                self.type = 1
            case 2:
                if tmp[max(tmp, key=tmp.get)] == 4:
                    self.type = 2
                else:
                    self.type = 3
            case 3:
                if tmp[max(tmp, key=tmp.get)] == 3:
                    self.type = 4
                else:
                    self.type = 5
            case 4:
                self.type = 6
            case 5:
                self.type = 7
            case _:
                self.type = 8

    def __gt__(self, __o: object) -> bool:
        if self.type == __o.type:
            for index, card in enumerate(self.cards):
                if self.strengths[card] == self.strengths[__o.cards[index]]:
                    continue
                elif self.strengths[card] > self.strengths[__o.cards[index]]:
                    return True
                else:
                    return False
        elif self.type < __o.type:
            return True
        else:
            return False

    def __str__(self) -> str:
        return self.cards


def rank_hand(answers, left, right, hand) -> int:
    if len(answers) == 0:
        return 0

    while left <= right:
        mid = left + (right - left) // 2

        if right == left:
            return mid
        elif answers[mid] > hand:
            right = mid
        else:
            left = mid + 1

    return 0


def camel_cards_part_one(input) -> int:
    lines = input.readlines()
    answers = []

    for line in lines:
        hand = Hand(line.split())
        index = rank_hand(answers, 0, len(answers), hand)
        answers.insert(index, hand)

    answer = 0
    rank = 1
    for hand in answers:
        answer += hand.bid * rank
        rank += 1

    return answer


def camel_cards_part_two(input) -> int:
    pass


def main() -> None:
    if len(argv) > 1:
        if argv[1] == "test":
            input = open("test.txt", "r")
        else:
            input = open("input.txt", "r")
    else:
        input = open("input.txt", "r")

    print("Camel Cards part one answer:", camel_cards_part_one(input))
    input.seek(0)
    print("Camel Cards part two answer:", camel_cards_part_two(input))


if __name__ == "__main__":
    main()
