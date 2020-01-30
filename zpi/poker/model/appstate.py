from enum import Enum


class AppState(Enum):
    READY = 0
    GAME_FINISHED = 1
    COMPUTER_PLAYING = 2
    USER_PLAYING = 3
    GAME_EVALUATE = 4