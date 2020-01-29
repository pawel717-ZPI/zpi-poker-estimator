from tkinter import *
from zpi.poker.logic import gamelogic, poker
from zpi.poker.view.frames import GameBoardFrame


class PokerGUI:
    def __init__(self, master):
        master.title('Poker')
        self.master = master
        self.points = None
        self.card_dict = {}
        self.load_card_images()

        self.game_board_frame = GameBoardFrame(master, relief="sunken", borderwidth=1, background="#08a131")
        self.game_board_frame.grid(row=0, column=0, sticky='ew', columnspan=15, rowspan=4)

        # self.player_score_label = IntVar()
        # Label(self.game_board_frame, text="Score:", background="#08a131", fg="white").grid(row=2, column=3, sticky='e')
        # Label(self.game_board_frame, textvariable=self.player_score_label, background="#08a131", fg="white").grid(row=2,
        #                                                                                                           column=4,
        #                                                                                                           sticky='w')
        # self.obscure_board()
        self.display_hand()
        self.create_buttons()
        self.__create_game_end_frame__()
        self.state = 0

    def create_buttons(self):
        self.call_button = Button(self.game_board_frame, text="Call", command=self.play)
        self.call_button.grid(row=2, column=5)
        self.fold_button = Button(self.game_board_frame, text="Fold", command=self.play)
        self.fold_button.grid(row=2, column=6)

    def play(self):

        if self.state == 0:
            self.display_board()
            self.display_other_hands()
            (self.points, myHand, board, win) = poker.game(self.hand, self.board, self.hands)
            self.display_points()
            self.show_game_end_frame(win)
            self.state = 1
        else:
            gamelogic.cardsList = poker.shuffle()
            self.__init__(self.master)

    def __create_game_end_frame__(self):
        self.game_end_frame = Frame(self.master, relief="raised", borderwidth=3, background="#035e18")
        self.winner_label = Label(self.game_end_frame, background="#035e18", fg="white")
        self.winner_label.grid(row=0, column=0, padx=(100, 100), pady=(30, 10))
        Button(self.game_end_frame, text="Okay", command=self.game_end_okay_callback) \
            .grid(row=1, column=0, padx=(100, 100), pady=(10, 30))

    def show_game_end_frame(self, winner):
        self.game_end_frame.grid(row=0, column=0, columnspan=15, rowspan=4)
        self.winner_label.config(text="The winner is player No. {}".format(winner))

    def hide_game_end_frame(self):
        self.game_end_frame.grid_remove()

    def game_end_okay_callback(self):
        self.hide_game_end_frame()
        self.reset_card_frame()

    def reset_card_frame(self):
        gamelogic.cardsList = poker.shuffle()
        self.__init__(self.master)

    def load_card_images(self):
        suits = ['heart', 'club', 'diamond', 'spade']
        face_cards = ['jack', 'queen', 'king']

        extension = 'ppm'
        folder = 'cards'
        self.card_dict['b'] = PhotoImage(file=folder + '/back.png')

        # aces
        self.card_dict['Ac'] = PhotoImage(file=folder + '/1_club.' + extension)
        self.card_dict['Ad'] = PhotoImage(file=folder + '/1_diamond.' + extension)
        self.card_dict['Ah'] = PhotoImage(file=folder + '/1_heart.' + extension)
        self.card_dict['As'] = PhotoImage(file=folder + '/1_spade.' + extension)

        # tens
        self.card_dict['Tc'] = PhotoImage(file=folder + '/10_club.' + extension)
        self.card_dict['Td'] = PhotoImage(file=folder + '/10_diamond.' + extension)
        self.card_dict['Th'] = PhotoImage(file=folder + '/10_heart.' + extension)
        self.card_dict['Ts'] = PhotoImage(file=folder + '/10_spade.' + extension)

        for suit in suits:
            # cards 2 to 9
            for card in range(1, 10):
                name = '{}/{}_{}.{}'.format(folder, str(card), suit, extension)
                image = PhotoImage(file=name)
                key = str(card) + suit[0]
                self.card_dict[key] = image

            # face cards
            for card in face_cards:
                name = '{}/{}_{}.{}'.format(folder, str(card), suit, extension)
                image = PhotoImage(file=name)
                key = card[0].upper() + suit[0]
                self.card_dict[key] = image


    def display_board(self):

        board = poker.board()
        self.board = board

        for i in range(len(board)):
            Label(self.game_board_frame, image=self.card_dict[board[i]], relief='raised').grid(row=1, column=i, pady=10)

    def display_hand(self):
        hand = poker.myHand()
        self.hand = hand

        for i in range(len(hand)):
            Label(self.game_board_frame, image=self.card_dict[hand[i]], relief='raised').grid(row=2, column=i, pady=10)

    def display_other_hands(self):
        hands = poker.anotherHands()
        self.hands = hands

        col = 0
        for i in range(5):
            hand = hands[i]
            Label(self.game_board_frame, image=self.card_dict[hand[0]], relief='raised').grid(row=0, column=col, pady=10)
            col += 1
            Label(self.game_board_frame, image=self.card_dict[hand[1]], relief='raised').grid(row=0, column=col, pady=10)
            col += 1

    # def obscure_other_hands(self):
    #     for i in range(10):
    #         Label(self.game_board_frame, image=self.card_dict['b'], relief='raised').grid(row=0, column=i, pady=10)

    def display_points(self):
        self.player_score_label.set(self.points[0])
