import interface
from interface import *
from language_dictionary import *
from lv_2 import map_l2
from lv_1 import callbacks_l1 as c

global ll1

global ll2

ll1 = False

ll2 = False


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
        {"text": translations["level_selection"][i.lang], "callback": level_selector},
        {"text": translations["quit_game"][i.lang], "callback": end_game}
    ]
    return actions


def level_game_actions():
    """Restituisce le azioni possibili nella schermata di inizio gioco."""
    actions = [
        {"text": translations["lev_1"][i.lang], "callback": level_1},
        {"text": translations["lev_2"][i.lang], "callback": level_2},
        {"text": translations["quit_game"][i.lang], "callback": end_game}
    ]
    return actions


def level_selector():
    i.create_buttons(level_game_actions())


def class_selector():
    i.create_buttons(class_actions())


def class_actions():
    actions = [
        {"text": translations["warrior"][i.lang], "callback": warrior},
        {"text": translations["mage"][i.lang], "callback": mage}
    ]
    return actions

def level_1():
    global ll1
    ll1 = True
    i.create_buttons(class_actions())


def level_2():
    global ll2
    ll2 = True
    i.create_buttons(class_actions())


def warrior():
    global ll1, ll2
    pg.Warrior()
    if ll1 is True:
        #ll1 = False
        c.go_04()
    elif ll2 is True:
        #ll2 = False
        map_l2.level_2(interface.i)


def mage():
    global ll1, ll2
    pg.Mage()
    if ll1 is True:
        #ll1 = False
        c.go_04()
    elif ll2 is True:
        #ll2 = False
        map_l2.level_2(interface.i)


def end_game():
    i.window.destroy()