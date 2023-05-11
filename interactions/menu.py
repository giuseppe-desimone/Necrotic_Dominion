from interface import * 
from language_dictionary import *
from lv_1 import callbacks_l1 as c

def new_play():
    i.image_wand("./media/start_screen")
    i.show_text("                                   " +
              "---------------------------------  " +
              "----------- Necrotic ------------  " +
              "---------               ---------  " +
              "----------- Dominion ------------  " +
              "---------------------------------  " +
              "                                   " +
              "                                   " +
              "                                   " +
              "           |  v0.12  |             " +
              "                                   ")
    i.create_buttons(start_game_actions())
    i.window.mainloop()


def start_game_actions():
    """Restituisce le azioni possibili nella schermata di inizio gioco."""
    actions = [
        {"text": translations["class_selection"][i.lang], "callback": class_caller},
        {"text": translations["quit_game"][i.lang], "callback": end_game}
    ]
    return actions


def class_caller():
    i.create_buttons(class_actions())


def class_actions():
    actions = [
        {"text": translations["warrior"][i.lang], "callback": warrior},
        {"text": translations["mage"][i.lang], "callback": mage}
    ]
    return actions


def end_game():
    i.window.destroy()


def warrior():
    pg.Warrior()
    c.go_04()

def mage():
    pg.Mage()
    c.go_34()
