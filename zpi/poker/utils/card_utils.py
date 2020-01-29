import random

from zpi.poker.logic.gamelogic import cardsList


def fill_community_card(base_cards, used_card):
    need_num = 5 - len(base_cards)
    return base_cards + pick_unused_card(need_num, used_card)


def pick_unused_card(card_num, used_card):
    unused = [card for card in cardsList if card not in used_card]
    choiced = random.sample(unused, card_num)
    return choiced


def pypoker_card_to_my_card(pypoker_card):
    return pypoker_card[1] + pypoker_card[0].lower()
