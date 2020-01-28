from tkinter import *

import poker

root = Tk()


class PokerGUI:
    def __init__(self, master):
        master.title('Poker')

        self.card_dict = {}
        self.load_card_images()

        self.card_frame = Frame(master, relief="sunken", borderwidth=1, background="green")
        self.card_frame.grid(row=0, column=0, sticky='ew', columnspan=15, rowspan=4)

        self.player_score_label = IntVar()
        Label(self.card_frame, text="Score:", background="green", fg="white").grid(row=2, column=3, sticky='e')
        Label(self.card_frame, textvariable=self.player_score_label, background="green", fg="white").grid(row=2, column=4, sticky='w')

        self.display_other_hands()
        self.display_board()
        self.display_hand()

        (self.points, myHand, board) = poker.game(self.hand, self.board, self.hands)

        self.display_points()


    def load_card_images(self):
        suits = ['heart', 'club', 'diamond', 'spade']
        face_cards = ['jack', 'queen', 'king']

        extension = 'ppm'
        folder = 'cards'

        #self.card_dict['b'] = PhotoImage(file=folder+'/back.png')

        # aces
        self.card_dict['Ac'] = PhotoImage(file=folder+'/1_club.' + extension)
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
            Label(self.card_frame, image=self.card_dict[board[i]], relief='raised').grid(row=1, column=i, pady=10)

    def display_hand(self):

        hand = poker.myHand()
        self.hand = hand

        for i in range(len(hand)):
            Label(self.card_frame, image=self.card_dict[hand[i]], relief='raised').grid(row=2, column=i, pady=10)

    def display_other_hands(self):
        hands = poker.anotherHands()
        self.hands = hands

        col = 0
        for i in range(5):
            print(i, ' ', col)
            hand = hands[i]
            Label(self.card_frame, image=self.card_dict[hand[0]], relief='raised').grid(row=0, column=col, pady=10)
            col+=1
            print(i, ' ', col)
            Label(self.card_frame, image=self.card_dict[hand[1]], relief='raised').grid(row=0, column=col, pady=10)
            col+=1

    def display_points(self):
        self.player_score_label.set(self.points[0])


pokerGUI = PokerGUI(root)

# print(pokerGUI.card_dict)
root.mainloop()