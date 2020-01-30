import random

from zpi.poker.bot.poker_bot import PokerBot
from zpi.poker.logic import gamelogic
from zpi.poker.logic.gamelogic import checkAllCombinations
from zpi.poker.model.appstate import AppState


def shuffle():
    return ['Ac', 'Ad', 'Ah', 'As', '2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d',
            '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h',
            '8s', '9c', '9d', '9h', '9s', 'Tc', 'Td', 'Th', 'Ts', 'Jc', 'Jd', 'Jh', 'Js', 'Qc', 'Qd', 'Qh', 'Qs',
            'Kc', 'Kd', 'Kh', 'Ks']


def myHand():
    first = random.choice(gamelogic.cardsList)
    gamelogic.cardsList.remove(first)
    second = random.choice(gamelogic.cardsList)
    gamelogic.cardsList.remove(second)
    hand = [first, second]
    return hand


def board():
    first = random.choice(gamelogic.cardsList)
    gamelogic.cardsList.remove(first)
    second = random.choice(gamelogic.cardsList)
    gamelogic.cardsList.remove(second)
    third = random.choice(gamelogic.cardsList)
    gamelogic.cardsList.remove(third)
    fourth = random.choice(gamelogic.cardsList)
    gamelogic.cardsList.remove(fourth)
    fifth = random.choice(gamelogic.cardsList)
    gamelogic.cardsList.remove(fifth)
    board = [first, second, third, fourth, fifth]
    return board


def anotherHands():
    hands = []
    for i in range(5):
        first = random.choice(gamelogic.cardsList)
        gamelogic.cardsList.remove(first)
        second = random.choice(gamelogic.cardsList)
        gamelogic.cardsList.remove(second)
        hand = [first, second]
        hands.append(hand)
    return hands


def game(myHand, board, anotherHands):
    points = []
    cards = [myHand + board]
    win = 0
    for l in range(len(anotherHands) + 1):
        points.append(0)
    for i in range(len(anotherHands)):
        cards.append(anotherHands[i] + board)
    for j in range(len(anotherHands) + 1):
        points[j] = checkAllCombinations(cards[j])
    for k in range(len(anotherHands) + 1):
        if points[k] == max(points):
            win = k

    return [points, myHand, board, win]


def monteCarlo(myHand):
    win = 0
    for i in range(1000):
        gamelogic.cardsList = shuffle()
        gamelogic.cardsList.remove(myHand[0])
        gamelogic.cardsList.remove(myHand[1])
        g = game(myHand, board(), anotherHands())
        if g[0][0] == max(g[0]):
            win = win + 1
    return str(win / 10) + '%'


def createCSV():
    file = open("pokerData.csv", "a")
    for i in range(100000):
        gamelogic.cardsList = shuffle()
        win = 0
        points = game(myHand(), board(), anotherHands())
        if points[0][0] == max(points[0]):
            win = 1
        element = points[1]
        for i in range(2):
            file.write(element[i])
            file.write(",")
        file.write(str(win))
        file.write("\n")


class Game:
    def __init__(self, num_players=6):
        self.num_players = num_players
        computer_players_hands = anotherHands()
        self.user_action = None
        self.user_hand = myHand()
        self.board = board()
        self.computer_players = [PokerBot(computer_players_hands[i], num_players, uid=i) for i in
                                 range(num_players - 1)]
        self.players_iterator = iter(self.computer_players)
        self.points = []
        self.state = AppState.READY

    def continue_game(self):
        current_player = self.players_iterator.__next__()
        return current_player.declare_action(self.get_valid_actions(), current_player.my_hole, self.board)

    def get_valid_actions(self):
        valid_actions = [{'action': 'fold', 'amount': 0}, {'action': 'call', 'amount': 10}]
        return valid_actions

    def evaluate(self):
        cards = [(player.my_hole + self.board, player.uid) for player in self.computer_players if
                 player.done_action == 'call']
        if self.user_action == 'call':
            cards.append((self.user_hand + self.board, "user"))
        self.winner = None
        max_points = 0

        for j in range(len(cards)):
            self.points.append(checkAllCombinations(cards[j][0]))
            if self.points[j] > max_points:
                max_points = self.points[j]
                self.winner = cards[j][1]

        return self.winner
