from interface import *
from language_dictionary import *


class Action():
    def __init__(self, description, action, i, action_arg=None, activation=lambda x:x, arg=True, repeat=True, matrix=None, room=None):
        self.text = description
        self.action = action
        self.i = i
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
            self.action(self.activation_arg, self.i)  # Pass the 'i' argument here
        else:
            self.action(self.i)  # Pass the 'i' argument here
        self.matrix[self.room[0]][self.room[1]].render(self.i)  # Pass the 'i' instance to the render() method

    def raw(self):
        if self.can_be_done:
            if self.activation(self.arg):
                return { "text":self.text, "callback":self.callback}
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

    def action(self, description, callback, i, action_arg=None, activation=lambda x: x, arg=True, repeat=True,
               matrix=None, room=None):
        self.actions.append(Action(description, callback, i, action_arg, activation, arg, repeat, matrix, room))
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

    def render(self, i):  # Add the 'i' argument to the render() method
        render_text = self.description
        actions = []

        for action in self.actions:
            actions.append(action.raw())

        if self.enemy:
            render_text += self.enemy.description
            for action in self.enemy.actions:
                actions.append(action.raw())

        if self.item:
            render_text += objects_translations[self.item.id][i.lang]
            for action in self.item.actions:
                actions.append(action.raw())

        i.image_wand(self.img)
        i.show_text(render_text)
        i.create_buttons(actions)

    def action(self, description, callback, i, action_arg=None, activation=lambda x:x, arg=True, repeat=True, matrix=None, room=None):
        self.actions.append(Action(description, callback, i, action_arg, activation, arg, repeat, matrix, room))
        return self


class Combat:
    def __init__(self, description, img, enemy):
        self.description = description
        self.img = img
        self.enemy = enemy

    def render(self, pg_actions):
        render_text = self.description
        actions = []

        render_text+=self.enemy.description

        for action in pg_actions:
            actions.append(action.raw())

        i.image_wand(self.img)
        i.show_text(render_text)
        i.create_buttons(actions)
