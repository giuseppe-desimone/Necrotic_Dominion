from interface import *

class Action():
    def __init__(self, description, action, activation=lambda x:x, arg=True, repeat=True):
        self.text = description
        self.action = action
        self.activation = activation
        self.arg = arg
        self.can_be_done = True
        self.repeat = repeat

    def callback(self):
        self.done()
        self.action()

    def raw(self):
        if self.can_be_done:
            if self.activation(self.arg):
                return { "text":self.text, "callback":self.callback }
        return {}

    def done(self):
        if not self.repeat:
            print("done")
            self.can_be_done = False
        

class Item():
    def __init__(self):
        self.id = ""
        self.description = ""
        self.bonus = {}
        self.action = None

    def action(self, description, callback, activation=lambda x:x, arg=True, repeat=True):
        self.action = Action(description, callback, activation, arg, repeat)


class Room:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.description = None
        self.img = None
        self.items = []
        self.enemy = None
        self.actions = []

    def render(self):
        render_text = self.description
        actions = []

        for action in self.actions:
            actions.append(action.raw())

        if self.enemy:
            render_text+=self.enemy.description
            for action in self.enemy.actions:
                actions.append(action.raw())
        
        for item in self.items:
            render_text += item.description
            for action in item.actions:
                actions.append(action.raw())

        i.image_wand(self.img)
        i.show_text(render_text)
        i.create_buttons(actions)

    def action(self, description, callback, activation=lambda x:x, arg=True, repeat=True):
        self.actions.append(Action(description,callback,activation,arg,repeat))
        return self

matrix_l2 = [[Room(X=i, Y=j) for j in range(9)] for i in range(9)]



###########################


matrix_l2[0][1].description="boh"
matrix_l2[0][1].img = "./media/img_lv1/05"

matrix_l2[0][1].action(
        "Torna indietro",
        matrix_l2[0][0].render, 
    )


matrix_l2[0][0].description="testt"
matrix_l2[0][0].img = "./media/img_lv1/06"


matrix_l2[0][0].action(
        "Vai avanti",
        matrix_l2[0][1].render, 
    )

matrix_l2[0][0].action(
        "cerca tra i resti",
        matrix_l2[0][0].render,
        activation=lambda enemy_life: enemy_life<0, 
        arg=-1,
        repeat=False
    )

###########################

matrix_l2[0][0].render()
