import random


cardsList = ['Ac', 'Ad', 'Ah', 'As', '2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d',
             '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s',
             '9c', '9d', '9h', '9s', 'Tc', 'Td', 'Th', 'Ts', 'Jc', 'Jd', 'Jh', 'Js', 'Qc', 'Qd', 'Qh', 'Qs', 'Kc',
             'Kd', 'Kh', 'Ks']

rankDict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
            'A': 14}

colorDict = {'c': 1, 'd': 2, 'h': 3, 's': 4}


def shuffle():
    global cardsList
    cardsList = ['Ac', 'Ad', 'Ah', 'As', '2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d',
                 '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h',
                 '8s', '9c', '9d', '9h', '9s', 'Tc', 'Td', 'Th', 'Ts', 'Jc', 'Jd', 'Jh', 'Js', 'Qc', 'Qd', 'Qh', 'Qs',
                 'Kc', 'Kd', 'Kh', 'Ks']


def myHand():
    first = random.choice(cardsList)
    cardsList.remove(first)
    second = random.choice(cardsList)
    cardsList.remove(second)
    hand = [first, second]
    return hand


def board():
    first = random.choice(cardsList)
    cardsList.remove(first)
    second = random.choice(cardsList)
    cardsList.remove(second)
    third = random.choice(cardsList)
    cardsList.remove(third)
    fourth = random.choice(cardsList)
    cardsList.remove(fourth)
    fifth = random.choice(cardsList)
    cardsList.remove(fifth)
    board = [first, second, third, fourth, fifth]
    return board


def anotherHands():
    hands = []
    for i in range(5):
        first = random.choice(cardsList)
        cardsList.remove(first)
        second = random.choice(cardsList)
        cardsList.remove(second)
        hand = [first, second]
        hands.append(hand)
    return hands


def pointsFromCards(cards):
    points = 0
    if cards[0] == 0:
        return 0
    for i in range(5):
        points = points + cards[1][i]
    points = points + 100 * cards[0]
    return points


def color(cards):
    colors = [0, 0, 0, 0]
    types = []
    for card in cards:
        if card[1] == 'c':
            colors[0] = colors[0] + 1
        if card[1] == 'd':
            colors[1] = colors[1] + 1
        if card[1] == 'h':
            colors[2] = colors[2] + 1
        if card[1] == 's':
            colors[3] = colors[3] + 1
    for i in range(4):
        if colors[i] >= 5:
            for card in cards:
                if list(colorDict.keys())[i] == card[1]:
                    types.append(rankDict[card[0]])
            return [6, types]
    return [0, 0]


def straight(cards):
    types = []
    for card in cards:
        types.append(rankDict[card[0]])
    types = list(set(types))
    if len(types) == 7:
        if types[6] == types[5] + 1 == types[4] + 2 == types[3] + 3 == types[2] + 4:
            return [5, types[2:7]]
        elif types[5] == types[4] + 1 == types[3] + 2 == types[2] + 3 == types[1] + 4:
            return [5, types[1:6]]
        elif types[4] == types[3] + 1 == types[2] + 2 == types[1] + 3 == types[0] + 4:
            return [5, types[0:5]]
        else:
            return [0, 0]
    elif len(types) == 6:
        if types[5] == types[4] + 1 == types[3] + 2 == types[2] + 3 == types[1] + 4:
            return [5, types[1:6]]
        elif types[4] == types[3] + 1 == types[2] + 2 == types[1] + 3 == types[0] + 4:
            return [5, types[0:5]]
        else:
            return [0, 0]
    elif len(types) == 5:
        if types[4] == types[3] + 1 == types[2] + 2 == types[1] + 3 == types[0] + 4:
            return [5, types[0:5]]
        else:
            return [0, 0]
    else:
        return [0, 0]


def flush(cards):
    if color(cards)[0] > 0:
        if straight(cards)[0] > 0:
            return [10, straight(cards)[1]]
        else:
            return [0, 0]
    else:
        return [0, 0]


def highCards(cards):
    types = []
    for card in cards:
        types.append(rankDict[card[0]])
    types.remove(min(types))
    types.remove(min(types))
    return [1, types]


def four(cards):
    counter = []
    for i in range(13):
        counter.append(0)
    allTypes = []
    types = []
    for i in range(len(cards)):
        counter[rankDict[cards[i][0]] - 2] = counter[rankDict[cards[i][0]] - 2] + 1
    for i in range(13):
        if counter[i] == 4:
            for card in cards:
                if rankDict[card[0]] == i + 2:
                    types.append(rankDict[card[0]])
            for card in cards:
                allTypes.append(rankDict[card[0]])
            rest = [x for x in allTypes if x not in types]
            types.append(max(rest))
            return [8, types]
    return [0, 0]


def three(cards):
    counter = []
    for i in range(13):
        counter.append(0)
    types = []
    sum = []
    for i in range(len(cards)):
        counter[rankDict[cards[i][0]] - 2] = counter[rankDict[cards[i][0]] - 2] + 1
    for i in range(13):
        if counter[i] == 3:
            sum.append(i)
    if len(sum) >= 1:
        types.append(max(sum) + 2)
        types.append(max(sum) + 2)
        types.append(max(sum) + 2)
        return [4, types]
    else:
        return [0, 0]


def restToThree(cards, three):
    if three[0] == 0:
        return [0, 0]
    allTypes = []
    for card in cards:
        allTypes.append(rankDict[card[0]])
    restOfCards = [x for x in allTypes if x not in three[1]]
    allCards = three[1] + [max(restOfCards)]
    restOfCards.remove(max(restOfCards))
    allCards = allCards + [max(restOfCards)]
    return [4, allCards]


def pair(cards):
    counter = []
    for i in range(13):
        counter.append(0)
    types = []
    sum = []
    for i in range(len(cards)):
        counter[rankDict[cards[i][0]] - 2] = counter[rankDict[cards[i][0]] - 2] + 1
    for i in range(13):
        if counter[i] == 2:
            sum.append(i)
    if len(sum) == 1:
        types.append(sum[0] + 2)
        types.append(sum[0] + 2)
        return [2, types]
    if len(sum) == 2:
        types.append(sum[0] + 2)
        types.append(sum[0] + 2)
        types.append(sum[1] + 2)
        types.append(sum[1] + 2)
        return [3, types]
    if len(sum) == 3:
        sum.remove(min(sum))
        types.append(sum[0] + 2)
        types.append(sum[0] + 2)
        types.append(sum[1] + 2)
        types.append(sum[1] + 2)
        return [3, types]
    else:
        return [0, 0]


def restToPairs(cards, pairs):
    allTypes = []
    for card in cards:
        allTypes.append(rankDict[card[0]])
    restOfCards = [x for x in allTypes if x not in pairs[1]]
    allCards = pairs[1] + [max(restOfCards)]
    if pairs[0] == 0:
        return [0, 0]
    if len(allCards) == 5:
        return [3, allCards]
    else:
        restOfCards.remove(max(restOfCards))
        allCards = allCards + [max(restOfCards)]
        restOfCards.remove(max(restOfCards))
        allCards = allCards + [max(restOfCards)]
        return [2, allCards]


def full(cards):
    p = 0
    if three(cards)[0] > 0:
        if pair(cards)[0] == 2:
            return [7, three(cards)[1] + pair(cards)[1]]
        if pair(cards)[0] == 3:
            p = pair(cards)[1]
            p.remove(min(p))
            p.remove(min(p))
            return [7, three(cards)[1] + p]
        else:
            return [0, 0]
    else:
        return [0, 0]


def checkAllCombinations(cards):
    points = 0
    if flush(cards)[0] > 0:
        points = pointsFromCards(flush(cards))
    elif four(cards)[0] > 0:
        points = pointsFromCards(four(cards))
    elif full(cards)[0] > 0:
        points = pointsFromCards(full(cards))
    elif color(cards)[0] > 0:
        points = pointsFromCards(color(cards))
    elif straight(cards)[0] > 0:
        points = pointsFromCards(straight(cards))
    elif three(cards)[0] > 0:
        points = pointsFromCards(restToThree(cards, three(cards)))
    elif pair(cards)[0] > 0:
        points = pointsFromCards(restToPairs(cards, pair(cards)))
    else:
        points = pointsFromCards(highCards(cards))
    return points


def game(myHand, board, anotherHands):
    points = [0, 0, 0, 0, 0, 0]
    cards = []
    cards.append(myHand + board)
    for i in range(5):
        cards.append(anotherHands[i] + board)
    for j in range(6):
        points[j] = checkAllCombinations(cards[j])
    return [points, myHand, board]



def createCSV():
    file = open("pokerData.csv", "a")
    element = []
    for i in range(100000):
        shuffle()
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


createCSV()

# win = [0, 0, 0, 0, 0, 0]
# for i in range(10000):
#     shuffle()
#     g = game(myHand(), board(), anotherHands())
#     for j in range(6):
#         if g[0][j] == max(g[0]):
#             win[j] = win[j] + 1
#             break
#
# print(win)
# print(sum(win))

# myHand=myHand()
# board=board()
# anotherHands=anotherHands()
# print(myHand)
# print(board)
# print(anotherHands)
# print(game(myHand,board,anotherHands))


# flushHand = ['2s', 'Js', 'Ts', 'Jd', 'Qs', 'Ks', '9s']
# print(checkAllCombinations(flushHand))
# print(flush(flushHand))
# print(pointsFromCards(flush(flushHand)))

# fourHand = ['As', 'Ad', 'Ah', 'Ac', 'Qs', 'Ks', '9s']
# fourHand = ['4d', 'Qs', '2s', '2h', '6s', 'Ks', 'Kc']
# print(checkAllCombinations(fourHand))
# print(four(fourHand))
# print(pointsFromCards(four(fourHand)))

# fullHand= ['As', 'Ad', 'Ac', 'Jd', 'Js','Ks','9s']
# print(checkAllCombinations(fullHand))
# print(full(fullHand))
# fullHand= ['As', 'Ad', 'Ac', 'Jd', 'Js','Ks','Ks']
# print(pointsFromCards(full(fullHand)))

# colorHand = ['As', 'Ks', 'Ah', '2s', 'Qs', 'Kd', '9s']
# print(checkAllCombinations(flushHand))
# print(color(colorHand))
# print(pointsFromCards(color(colorHand)))

# straightHand = ['As', 'Ad', 'Jh', 'Tc', 'Qs', 'Ks', '9d']
# straightHand = ['9h', '9c', '9s', '6s', '3h', '3d', '7h']
# straightHand = myHand() + board()
# print(straightHand)
# print(checkAllCombinations(straightHand))
# print(straight(straightHand))
# print(pointsFromCards(straight(straightHand)))

# threeHand = ['As', 'Ad', 'Ah', 'Tc', 'Qs', 'Ks', '9d']
# print(checkAllCombinations(flushHand))
# print(three(threeHand))
# print(restToThree(threeHand,three(threeHand)))
# print(pointsFromCards(restToThree(threeHand,three(threeHand))))

# twoPairHand = ['As', 'Ad', 'Jh', 'Jc', 'Qs', 'Ks', '9d']
# print(checkAllCombinations(flushHand))
# print(pair(twoPairHand))
# print(restToPairs(twoPairHand,pair(twoPairHand)))
# print(pointsFromCards(restToPairs(twoPairHand,pair(twoPairHand))))

# pairHand = ['As', 'Ad', '2h', 'Jc', 'Qs', 'Ks', '9d']
# print(checkAllCombinations(pairHand))
# print(pair(pairHand))
# print(restToPairs(pairHand,pair(pairHand)))
# print(pointsFromCards(restToPairs(pairHand,pair(pairHand))))
