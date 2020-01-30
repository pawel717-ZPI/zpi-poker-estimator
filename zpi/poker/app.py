from tkinter import Tk

from zpi.poker.view.poker_gui import PokerGUI

if __name__ == "__main__":
    root = Tk()
    pokerGUI = PokerGUI(root)
    root.mainloop()
