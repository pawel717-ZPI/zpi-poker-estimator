import random

from zpi.poker.bot.poker_bot import MyPokerBot
from zpi.poker.logic import gamelogic
from zpi.poker.logic.gamelogic import checkAllCombinations


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
    pokerBot = MyPokerBot()
    pokerBot.num_players = 5
    hole_card = anotherHands[0]
    round_state = {'community_card': board}
    # valid_actions = [{'action': 'fold', 'amount': 0}, {'action': 'call', 'amount': 10}, {'action': 'raise', 'amount': {'min': 15, 'max': 100}}]
    valid_actions = [{'action': 'fold', 'amount': 0}, {'action': 'call', 'amount': 10}]
    pokerBot.declare_action(valid_actions, hole_card, round_state)

    points = []
    cards = []
    cards.append(myHand + board)
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
