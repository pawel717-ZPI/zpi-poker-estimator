from pathlib import Path
from tkinter import PhotoImage


def get_project_root() -> Path:
    """Returns project root catalog."""
    return Path(__file__).parent.parent.parent.parent


def get_images_path() -> Path:
    """Returns images catalog."""
    return get_project_root().joinpath('images')


class ImageLoader:
    def __init__(self, images_path=get_images_path()):
        self.images_path = images_path

    def load_image(self, name):
        return PhotoImage(file=self.images_path.joinpath(name).__str__())


class CardsMapper:
    def __init__(self):
        self.suits_map = {'h': 'heart', 'c': 'club', 'd': 'diamond', 's': 'spade'}
        self.ranks_map = {'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': '1', 'T': '10'}

    def map_to_filename(self, card):
        filename_rank = self.ranks_map.get(card[0])
        filename_suit = self.suits_map.get(card[1])
        return (filename_rank if filename_rank else card[0]) + '_' + filename_suit + '.ppm'


class CardsLoader:
    def __init__(self):
        self.mapper = CardsMapper()
        self.image_loader = ImageLoader(images_path=get_images_path().joinpath('cards'))

    def load(self, cards):
        return {
            **{card: self.image_loader.load_image(self.mapper.map_to_filename(card)) for card in cards},
            'b': self.image_loader.load_image('back.png')
        }
