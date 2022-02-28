import math
import random

from Game.Action import Action
from Game.ForwardModel import ForwardModel
from Game.Heuristic import Heuristic
from Players.Player import Player


class NOTLAPlayer2(Player):
    def __init__(self):
        self.forward_model = ForwardModel()
        self.heuristic = Heuristic()

    def think(self, observation, budget):
        list_actions = observation.get_list_actions()
        player_id = observation.turn
        pos = observation.playing_cards.len()
        pos_initial = pos
        best_value = -math.inf
        best_action = None

        if pos_initial == 0 or pos_initial == 2:
            factor = 1
        else:
            factor = -1
        other_player = player_id
        for action in list_actions:
            new_obs = observation.clone()
            score_player = self.forward_model.play(new_obs, action, self.heuristic)
            if other_player == 3:
                other_player = 0
            else:
                other_player += 1
            while pos < 3:
                pos += 1
                if other_player == 4:
                    other_player = 0
                other_card = new_obs.hands[other_player].get_card(random.choice(range(new_obs.hands[other_player].len())))          # Selecciona una carta al azar de otro jugador
                other_action = Action(other_card)                                                   # Transfoma la carta elegida a una acción
                score = self.forward_model.play(new_obs, other_action, self.heuristic)              # Juega la carta del otro jugador
                value = score + score_player * factor
                if value >= best_value:
                    best_action = other_action
                    best_value = value
                other_player += 1

        return best_action



    def __str__(self):
        return "NOTLAPlayer2"