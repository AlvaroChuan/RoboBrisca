import math
import random

from Game.Action import Action
from Game.ForwardModel import ForwardModel
from Game.Heuristic import Heuristic
from Players.Player import Player
from Players.OSLAPlayer import OSLAPlayer

class QlearningPLayer (Player):

    def __init__(self):
        self.modelo = Modelo()
        self.modelo.read_from_disk("modelo.txt")

    def think(self, obs, budget):
        t = time()
        scores = [0,0,0]
        while time() - t() < budget - 0.2:
            new_obs = obs.get_randomized_clone()
            scores.append(self.modelo.get_scores(new_obs))

        if sum(scores) == 0:
            p = OSLAPlayer()
            return  p.think(obs, 0.15)

        index = get_max_score_index(scores)
        list_actions = obs.get_actions()
        return list_actions[index]

    def train(self):
        self.modelo.train(n_veces)