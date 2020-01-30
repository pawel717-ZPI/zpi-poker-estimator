from pypokerengine.players import BasePokerPlayer

from zpi.poker.bot.win_evaluator import estimate_win_rate


class PokerBot(BasePokerPlayer):
    def __init__(self, hole, num_players, uid):
        super().__init__()
        self.my_hole = hole
        self.num_players = num_players
        self.uid = uid
        self.done_action = None

    def declare_action(self, valid_actions, hole_cards, community_cards):
        # Estimate the win rate
        win_rate = estimate_win_rate(1000, self.num_players, hole_cards, community_cards)

        self.amount = None
        self.done_action = 'fold'

        # If the win rate is large enough, then raise
        win_rate = win_rate * (self.num_players - 1)
        if win_rate > 0.5:
            raise_options = [item for item in valid_actions if item['action'] == 'raise']
            if raise_options.__len__() != 0:
                self.check_raise_action(raise_options, win_rate)
        else:
            self.check_call_action(valid_actions)

        # Set the amount
        if self.amount is None:
            items = [item for item in valid_actions if item['action'] == self.done_action]
            self.amount = items[0]['amount']

        return {'action': self.done_action, 'amount': self.amount, 'uid': self.uid}

    def check_raise_action(self, raise_options, win_rate):
        if win_rate > 0.95 and raise_options is not None:
            # If it is extremely likely to win, then raise as much as possible
            self.done_action = 'raise'
            self.amount = raise_options[0]['amount']['max']
        elif win_rate > 0.90 and raise_options is not None:
            # If it is extremely likely to win, then raise as much as possible
            self.done_action = 'raise'
            self.amount = raise_options[0]['amount']['max'] / 2
        elif win_rate > 0.85 and raise_options is not None:
            # If it is likely to win, then raise by the minimum amount possible
            self.done_action = 'raise'
            self.amount = raise_options[0]['amount']['min']
        else:
            # If there is a chance to win, then call
            self.done_action = 'call'

    def check_call_action(self, valid_actions):
        # Check whether it is possible to call
        can_call = len([item for item in valid_actions if item['action'] == 'call']) > 0
        call_amount = [item for item in valid_actions if item['action'] == 'call'][0]['amount']
        if can_call and call_amount <= 10:
            self.done_action = 'call'
        else:
            self.done_action = 'fold'
