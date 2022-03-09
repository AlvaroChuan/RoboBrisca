
class Modelo:

    def __init__(self):
        self.q0 = dict ()
        self.q1 = dict ()
        self.q2 = dict ()



    def obs2fv(self,obs):
        #transformar obs en fv(vector)

    def train(self, n_veces):
        for i in range(n_veces):
            brisca_game.reset()
            #jugar hasta el final
            #(Cada vez que se juega una acción se actualiza el modelo)

    action = player.think()
    reward = fm.play(gs, action)
    Update modelo (gs antes, gs depues, accion, reward)
    if action == 0:
        self.q0[obs2fv(obs)] = nuevo valor


