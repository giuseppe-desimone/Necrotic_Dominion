from interface import *
from language_dictionary import *


class Action():
    def __init__(self, description, action, action_arg=None, activation=lambda x:x, arg=True, repeat=True, matrix=None, room=None):
        self.text = description
        self.action = action
        self.activation = activation
        self.activation_arg = action_arg
        self.arg = arg
        self.can_be_done = True
        self.repeat = repeat
        self.matrix=matrix
        self.room=room

    def callback(self):
        self.done()
        if self.activation_arg is not None:
            self.action(self.activation_arg)
        else:
            self.action()
        self.matrix[self.room[0]][self.room[1]].render() 

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
    def __init__(self, itemid, bonus = None):
        self.id = itemid
        self.bonus =bonus
        self.actions = []

    def action(self, description, callback, action_arg=None, activation=lambda x:x, arg=True, repeat=True, matrix=None, room=None):
        self.actions.append(Action(description, callback, action_arg, activation,arg, repeat, matrix, room))
        return self

class Room:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.description = None
        self.img = None
        self.item = None
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
        
        if self.item:
            render_text += objects_translations[self.item.id][i.lang]
            for action in self.item.actions:
                actions.append(action.raw())

        i.image_wand(self.img)
        i.show_text(render_text)
        i.create_buttons(actions)

    def action(self, description, callback, action_arg=None, activation=lambda x:x, arg=True, repeat=True, matrix=None, room=None):
        self.actions.append(Action(description, callback, action_arg, activation, arg, repeat, matrix, room))
        return self

matrix_l2 = [[Room(X=i, Y=j) for j in range(9)] for i in range(9)]


matrix_l2[0][4].description = "L’atrio del castello è spazioso, \ncon alti soffitti affrescati e \npareti di pietra che riflettono\nla luce. \n\nL’odore di fumo delle torce e di \ncera delle candele riempie \nl’aria, mentre i passi echeggiano \nsui pavimenti di marmo scuro. \n\nAi lati dell’atrio si trovano \ngrandi porte di quercia scolpite \na mano, una rivolta verso est e \nl’altra verso ovest. \n\nUn ampio corridoio si apre verso \nsud, con i lampadari appesi alle \npareti di pietra che illuminano \nil percorso e creano ombre \ndanzanti."
matrix_l2[0][4].img = "./media/img_lv1/04"
matrix_l2[0][4].item = Item("key0").action("Raccogli la chiave", pg.PG.item_pickup, "key0",repeat=False, matrix=matrix_l2, room=(0,4))
matrix_l2[0][4].action(
        "Vai ad est",
        matrix_l2[0][3].render,
        matrix=matrix_l2, room=(0,3)
    )


matrix_l2[0][3].description = "Nel cuore del castello si trova l’armeria, una vasta stanza dalle pareti in pietra ornate da \nantichi stemmi e scudi impolverati. \n\nUna volta custode di migliaia di armi e armature, ora le grandi mensole e gli armadi dell’armeria \nrimangono vuoti e silenziosi. \n\nUn’indicibile tristezza si respira nell’aria, interrotta solo dalla vista di una cassapanca in un \nangolo."
matrix_l2[0][3].img = "./media/img_lv1/03"
matrix_l2[0][3].action(
        "Vai a ovest",
        matrix_l2[0][4].render, 
        matrix=matrix_l2, room=(0,4)

    )


matrix_l2[0][4].render()


# ###########################


# matrix_l2[0][1].description="boh"
# matrix_l2[0][1].img = "./media/img_lv1/05"

# matrix_l2[0][1].action(
#         "Torna indietro",
#         matrix_l2[0][0].render, 
#     )


# matrix_l2[0][0].description="testt"
# matrix_l2[0][0].img = "./media/img_lv1/06"
# matrix_l2[0][0].action(
#         "Vai avanti",
#         matrix_l2[0][1].render, 

#     )

# matrix_l2[0][0].action(
#         "cerca tra i resti",
#         matrix_l2[0][0].render,
#         activation=lambda enemy_life: enemy_life<0, 
#         arg=-1,
#         repeat=False
#     )

# ###########################

# matrix_l2[0][0].render()
