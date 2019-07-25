#when a loop repeats an unknown number of times and ends when some condition is met, 
# which is what happens in a while loop. 
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []
while sum(hand)  < 17:
    hand.append(card_deck.pop())