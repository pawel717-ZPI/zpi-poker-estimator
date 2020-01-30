from enum import auto, Enum


class AppState(Enum):
    READY = auto
    GAME_FINISHED = auto
    PLAYING = auto