# from poker import shuffle, game, myHand, board, anotherHands, monteCarlo
# import gamelogic
# print(monteCarlo(['2c', '7d']))

# win = [0, 0, 0, 0, 0, 0]
# for i in range(100):
#     gamelogic.cardsList = shuffle()
#     g = game(myHand(), board(), anotherHands())
#     for j in range(6):
#         if g[0][j] == max(g[0]):
#             win[j] = win[j] + 1
from tkinter import Tk

from zpi.poker.view.poker_gui import PokerGUI

if __name__ == "__main__":
    root = Tk()
    pokerGUI = PokerGUI(root)
    root.mainloop()
