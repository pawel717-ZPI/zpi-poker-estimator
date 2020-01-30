from tkinter import Frame, Label, IntVar, Button, PhotoImage, StringVar

from zpi.poker.model import game_state
from zpi.poker.utils.file import get_images_path, ImageLoader, CardsLoader


class GameBoardFrame(Frame):
    def __init__(self, hand, **kw):
        super().__init__(**kw)
        self.__image_loader__ = ImageLoader()
        self.buttons = {}
        self.images = CardsLoader().load(game_state.all_cards)
        self.player_score_label = StringVar()
        self.__create_score_label__()
        self.__create_actions_label__()
        self.__create_board__()
        self.__create_other_hands__()
        self.__create_hand__(hand)
        self.__create_buttons__()

    def __create_other_hands__(self):
        for i in range(10):
            Label(self, image=self.images['b'], relief='raised').grid(row=0, column=i, pady=10)

    def __create_score_label__(self):
        Label(self, text="Score:", background="#08a131", fg="white").grid(row=2, column=3, sticky='e')
        Label(self, textvariable=self.player_score_label, background="#08a131", fg="white") \
            .grid(row=2, column=4, sticky='w')

    def __create_actions_label__(self):
        self.actions_label = Label(self, text="", background="#08a131", fg="white")
        self.actions_label.grid(row=3, column=5, columnspan=3)

    def __create_board__(self):
        for i in range(5):
            Label(self, image=self.images['b'], relief='raised').grid(row=1, column=i, pady=10)

    def __create_hand__(self, hand):
        for i in range(len(hand)):
            Label(self, image=self.images[hand[i]], relief='raised').grid(row=2, column=i, pady=10)

    def __create_buttons__(self):
        btn_call = Button(self, text="Call")
        btn_call.grid(row=2, column=5)
        btn_fold = Button(self, text="Fold")
        btn_fold.grid(row=2, column=6)
        btn_continue = Button(self, text="Continue")
        btn_continue.grid(row=2, column=7)
        self.buttons['call'] = btn_call
        self.buttons['fold'] = btn_fold
        self.buttons['continue'] = btn_continue
        self.hide_user_actions()

    def handle_game_action(self, action):
        txt = self.actions_label['text'] + "Player {} has done {}\n".format(action['uid'], action['action'])
        self.actions_label.config(text=txt)

    def display_points(self, points):
        self.player_score_label.set(points)

    def display_other_hands(self, hands):
        for i in range(5):
            hand = hands[i]
            col = i * 2
            Label(self, image=self.images[hand[0]], relief='raised').grid(row=0, column=col, pady=10)
            Label(self, image=self.images[hand[1]], relief='raised').grid(row=0, column=col + 1, pady=10)

    def display_board(self, board):
        for i in range(len(board)):
            Label(self, image=self.images[board[i]], relief='raised').grid(row=1, column=i, pady=10)

    def display_user_actions(self):
        self.buttons['call'].grid()
        self.buttons['fold'].grid()

    def hide_user_actions(self):
        self.buttons['call'].grid_remove()
        self.buttons['fold'].grid_remove()


class GameEndFrame(Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.buttons = {}
        self.__create_winner_label__()
        self.__create_buttons__()

    def __create_winner_label__(self):
        self.winner_label = Label(self, background="#035e18", fg="white")
        self.winner_label.grid(row=0, column=0, padx=(100, 100), pady=(30, 10))

    def __create_buttons__(self):
        btn_okay = Button(self, text="Okay")
        btn_okay.grid(row=1, column=0, padx=(100, 100), pady=(10, 30))
        self.buttons['okay'] = btn_okay

    def show(self, winner):
        self.grid(row=0, column=0, columnspan=15, rowspan=4)
        self.winner_label.config(text="The winner is player No. {}".format(winner))

    def hide(self):
        self.grid_remove()
