from tkinter import Frame, Label, IntVar, Button, PhotoImage


class GameBoardFrame(Frame):
    def __init__(self, hand):
        self.buttons = {}
        self.images = self.__load_card_images__()
        self.player_score_label = IntVar()
        self.__create_score_label__()
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

    def __create_board__(self):
        for i in range(5):
            Label(self, image=self.images['b'], relief='raised').grid(row=1, column=i, pady=10)

    def __create_hand__(self, hand):
        for i in range(len(hand)):
            Label(self, image=self.images[hand[i]], relief='raised').grid(row=2, column=i, pady=10)

    def __create_buttons__(self):
        btn_call = Button(self, text="Call", command=self.play)
        btn_call.grid(row=2, column=5)
        btn_fold = Button(self, text="Fold", command=self.play)
        btn_fold.grid(row=2, column=6)
        self.buttons['call'] = btn_call
        self.buttons['fold'] = btn_fold

    def __load_card_images__(self):
        suits = ['heart', 'club', 'diamond', 'spade']
        face_cards = ['jack', 'queen', 'king']

        extension = 'ppm'
        folder = 'cards'
        images = {}
        images['b'] = PhotoImage(file=folder + '/back.png')

        # aces
        images['Ac'] = PhotoImage(file=folder + '/1_club.' + extension)
        images['Ad'] = PhotoImage(file=folder + '/1_diamond.' + extension)
        images['Ah'] = PhotoImage(file=folder + '/1_heart.' + extension)
        images['As'] = PhotoImage(file=folder + '/1_spade.' + extension)

        # tens
        images['Tc'] = PhotoImage(file=folder + '/10_club.' + extension)
        images['Td'] = PhotoImage(file=folder + '/10_diamond.' + extension)
        images['Th'] = PhotoImage(file=folder + '/10_heart.' + extension)
        images['Ts'] = PhotoImage(file=folder + '/10_spade.' + extension)

        for suit in suits:
            # cards 2 to 9
            for card in range(1, 10):
                name = '{}/{}_{}.{}'.format(folder, str(card), suit, extension)
                image = PhotoImage(file=name)
                key = str(card) + suit[0]
                self.images[key] = image

            # face cards
            for card in face_cards:
                name = '{}/{}_{}.{}'.format(folder, str(card), suit, extension)
                image = PhotoImage(file=name)
                key = card[0].upper() + suit[0]
                self.images[key] = image

        return images

    def display_points(self, points):
        self.player_score_label.set(points)

    def display_other_hands(self, hands):
        for i in range(5):
            hand = hands[i]
            col = i * 2
            Label(self, image=self.images[hand[0]], relief='raised').grid(row=0, column=col + 1, pady=10)
            Label(self, image=self.images[hand[1]], relief='raised').grid(row=0, column=col + 2, pady=10)

    def display_board(self, board):
        for i in range(len(board)):
            Label(self.game_board_frame, image=self.images[board[i]], relief='raised').grid(row=1, column=i, pady=10)


class GameEndFrame(Frame):
    def __init__(self):
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

    def hide(self, winner):
        self.grid_remove()
