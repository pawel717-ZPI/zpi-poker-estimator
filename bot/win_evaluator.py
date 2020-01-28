from utils.card_utils import pick_unused_card, fill_community_card, pypoker_card_to_my_card
from poker import checkAllCombinations


def estimate_win_rate_pypoker(nb_simulation, nb_player, hole_card, community_card=None):
    if not community_card: community_card = []

    # TODO temporary, map pypoker cards to our cards representation
    hole_card = [pypoker_card_to_my_card(s) for s in hole_card]
    community_card = [pypoker_card_to_my_card(s) for s in community_card]

    win_count = sum([montecarlo_simulation(nb_player, hole_card, community_card) for _ in range(nb_simulation)])
    return 1.0 * win_count / nb_simulation


def estimate_win_rate(nb_simulation, nb_player, hole_card, community_card=None):
    if not community_card: community_card = []

    win_count = sum([montecarlo_simulation(nb_player, hole_card, community_card) for _ in range(nb_simulation)])
    return 1.0 * win_count / nb_simulation


def montecarlo_simulation(nb_player, hole_card, community_card):
    # Do a Monte Carlo simulation given the current state of the game by evaluating the hands
    community_card = fill_community_card(community_card, used_card=hole_card + community_card)
    unused_cards = pick_unused_card((nb_player - 1) * 2, hole_card + community_card)
    opponents_hole = [unused_cards[2 * i:2 * i + 2] for i in range(nb_player - 1)]
    opponents_score = [checkAllCombinations(hole + community_card) for hole in opponents_hole]
    my_score = checkAllCombinations(hole_card + community_card)
    return 1 if my_score >= max(opponents_score) else 0
