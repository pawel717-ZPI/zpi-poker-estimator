from examples.players.fish_player import FishPlayer
from examples.players.fold_man import FoldMan
from examples.players.honest_player import HonestPlayer
from examples.players.random_player import RandomPlayer
from pypokerengine.api.game import setup_config, start_poker

from zpi.poker.bot import MyPokerBot


def find_winner(game_result):
    winner = game_result['players'][0]
    for player in game_result['players']:
        if player['stack'] > winner['stack']:
            winner = player
    return winner


config = setup_config(max_round=100, initial_stack=100, small_blind_amount=5)
wins = {}
players = [(RandomPlayer(), 'p1'), (MyPokerBot(), 'p2'), (HonestPlayer(), 'p3'), (FishPlayer(), 'p4'),
           (FoldMan(), 'p5')]
for player in players:
    config.register_player(name=player[1], algorithm=player[0])
    wins[player[1]] = 0

for i in range(100):
    game_result = start_poker(config, verbose=0)
    print(game_result)
    winner = find_winner(game_result)
    wins[winner['name']] += 1
    print("winner is:", winner['name'])

print("end", wins)
