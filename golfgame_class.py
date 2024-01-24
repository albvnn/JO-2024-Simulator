
class GolfBall:
    def __init__(self, x, y):
        pos_x = x
        pos_y = y
        victory_condition = False

    def get_xpos(self):
        return self.pos_x

    def get_ypos(self):
        return self.pos_y

    def get_victory_condition(self):
        return self.victory_condition

    def victory(self):
        self.victory_condition = True
        return self.victory_condition

