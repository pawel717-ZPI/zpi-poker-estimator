from zpi.poker.logic import gamelogic, poker
from zpi.poker.model import game_state
from zpi.poker.view.frames import GameBoardFrame, GameEndFrame


class PokerGUI:
    def __init__(self, master):
        master.title('Poker')
        self.master = master
        self.points = None
        self.hand = poker.myHand()
        self.card_dict = {}

        self.game_board_frame = GameBoardFrame(master, relief="sunken", borderwidth=1, background="#08a131",
                                               hand=self.hand)
        self.game_board_frame.grid(row=0, column=0, sticky='ew', columnspan=15, rowspan=4)
        self.game_board_frame.buttons['call'].bind('', self.__play__)
        self.game_board_frame.buttons['fold'].bind('', self.__play__)
        self.__create_game_end_frame__()

    def __play__(self):
        if game_state.state == 0:
            self.__display_board__()
            self.__display_other_hands__()
            (self.points, myHand, board, winner) = poker.game(self.hand, self.board, self.hands)
            self.game_board_frame.display_points(self.points[0])
            self.game_end_frame.show(winner)
            game_state.state = 1
        else:
            gamelogic.cardsList = poker.shuffle()
            self.__init__(self.master)

    def __create_game_end_frame__(self):
        self.game_end_frame = GameEndFrame(self.master, relief="raised", borderwidth=3, background="#035e18")
        self.game_end_frame.buttons['okay'].bind('', self.__reset__)

    def __display_board__(self):
        self.board = poker.board()
        self.game_board_frame.display_board(self.board)

    def __display_other_hands__(self):
        self.hands = poker.anotherHands()
        self.game_board_frame.display_other_hands(self.hands)

    def __reset__(self):
        self.game_end_frame.hide()
        gamelogic.cardsList = poker.shuffle()
        self.__init__(self.master)
