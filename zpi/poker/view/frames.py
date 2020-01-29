from tkinter import Frame, Label, IntVar


class GameBoardFrame(Frame):
    def __init__(self):
        self.player_score_label = IntVar()
        self.__create_score_label__()
        self.__create_other_hands__()
        self.__create_board__()

    def __create_other_hands__(self):
        for i in range(10):
            Label(self, image=self.card_dict['b'], relief='raised').grid(row=0, column=i, pady=10)

    def __create_score_label__(self):
        Label(self, text="Score:", background="#08a131", fg="white").grid(row=2, column=3, sticky='e')
        Label(self, textvariable=self.player_score_label, background="#08a131", fg="white") \
            .grid(row=2, column=4, sticky='w')

    def __create_board__(self):
        for i in range(5):
            Label(self, image=self.card_dict['b'], relief='raised').grid(row=1, column=i, pady=10)

    def display_hand(self):
        hand = poker.myHand()
        self.hand = hand

        for i in range(len(hand)):
            Label(self, image=self.card_dict[hand[i]], relief='raised').grid(row=2, column=i, pady=10)
