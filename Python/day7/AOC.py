import re

CARD_RANKS = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

HANDS_TYPES = {
    "five_of_a_kind": 7,
    "four_of_a_kind": 6,
    "full_house": 5,
    "three_of_a_kind": 4,
    "two_pairs": 3,
    "one_pair": 2,
    "high_card": 1
}

class Player:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        
        self.hand_type, self.card_values = self.cal_hand(hand)
    
    def __str__(self):
        return f"{self.hand} is a {self.hand_type}, {self.card_values}, {self.bid}"
    
    # Learned about this today __lt__ from https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes-in-python
    # Pretty fucking useful
    def __lt__(self, other):
        # Compare players based on hand type, hand value, and card values
        if self.hand_type != other.hand_type:
            return HANDS_TYPES[self.hand_type] < HANDS_TYPES[other.hand_type]
        
        # Compare card values in case of a tie in hand type and hand value
        for self_card, other_card in zip(self.card_values, other.card_values):
            if self_card != other_card:
                return self_card < other_card
        
        return False
        
    def cal_hand(self, card):
        cards = {}
        card_vals = []
        h_type = "high_card"
        for c in card:
            card_vals.append(CARD_RANKS[c])
            if c in cards:
                cards[c] += 1
            else:
                cards[c] = 1
        hand_count = list(cards.values())
        hand_count.sort(reverse=True)
        
        if hand_count[0] == 5:
            h_type = "five_of_a_kind"
        elif hand_count[0] == 4:
            h_type = "four_of_a_kind"
        elif hand_count[0] == 3:
            if hand_count[1] == 2:
                h_type = "full_house"
            else:
                h_type = "three_of_a_kind"
        elif hand_count[0] == 2:
            if hand_count[1] == 2:
                h_type = "two_pairs"
            else:
                h_type = "one_pair"
        return h_type, card_vals
    
def parse_input(input):
    lines = input.splitlines()
    hands, bids = [], []
    for line in lines:
        line = line.split(" ")
        hands.append(line[0])
        bids.append(int(line[1]))
    return hands, bids
    
def part1(hands, bids):
    players = []
    sum = 0
    for hand, bid in zip(hands, bids):
        players.append(Player(hand, bid))

    players.sort()
    for rank, player in enumerate(players, start=1):
        sum += rank * player.bid
    return sum

def part2(input):
    return True

def main():
    input = open("input.txt", "r").read()
    hands, bids = parse_input(input)
    part1_sum = part1(hands, bids)
    part2_sum = 0
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()