from zpi.poker.logic import gamelogic, poker
from zpi.poker.logic.poker import Game, monteCarlo
from zpi.poker.model.appstate import AppState
from zpi.poker.view.frames import GameBoardFrame, GameEndFrame


class PokerGUI:
    def __init__(self, root):
        root.title('Poker')
        self.root = root
        self.points = None
        self.game = Game()
        self.hand = self.game.user_hand
        self.__create_game_board_frame__()
        self.__create_game_end_frame__()

    def __play__(self):
        if self.game.state == AppState.READY:
            self.__display_board__()
            self.game.state = AppState.COMPUTER_PLAYING
            return

        elif self.game.state == AppState.COMPUTER_PLAYING:
            try:
                self.game_board_frame.handle_game_action(self.game.continue_game())
                return
            except StopIteration:
                self.game_board_frame.buttons['continue'].grid_remove()
                self.game_board_frame.display_user_actions()
                self.game_board_frame.display_points(monteCarlo(self.game.user_hand))
                self.game.state = AppState.USER_PLAYING

        elif self.game.state == AppState.GAME_EVALUATE:
            self.__display_other_hands__()
            self.game.state = AppState.GAME_FINISHED
            self.game_end_frame.show(self.game.evaluate())
            return



    def __create_game_end_frame__(self):
        self.game_end_frame = GameEndFrame(master=self.root, relief="raised", borderwidth=3, background="#035e18")
        self.game_end_frame.buttons['okay'].config(command=self.__reset__)

    def __create_game_board_frame__(self):
        self.game_board_frame = GameBoardFrame(master=self.root, relief="sunken", borderwidth=1,
                                               background="#08a131", hand=self.hand)
        self.game_board_frame.grid(row=0, column=0, sticky='ew', columnspan=15, rowspan=4)
        self.game_board_frame.buttons['call'].config(command=self.__user_call__)
        self.game_board_frame.buttons['fold'].config(command=self.__user_fold__)
        self.game_board_frame.buttons['continue'].config(command=self.__play__)

    def __display_board__(self):
        self.board = self.game.board
        self.game_board_frame.display_board(self.board)

    def __display_other_hands__(self):
        self.hands = [player.my_hole for player in self.game.computer_players]
        self.game_board_frame.display_other_hands(self.hands)

    def __reset__(self):
        self.game.state = AppState.READY
        self.game_end_frame.hide()
        self.game_board_frame.grid_remove()
        gamelogic.cardsList = poker.shuffle()
        self.__init__(self.root)

    def __user_call__(self):
        self.__user_action__('call')

    def __user_fold__(self):
        self.__user_action__('fold')

    def __user_action__(self, action):
        self.game.user_action = action
        self.game.state = AppState.GAME_EVALUATE
        self.__play__()