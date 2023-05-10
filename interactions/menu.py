from interface import * 
from language_dictionary import *

def new_play():
    image_wand("./media/start_screen")
    show_text("                                   " +
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
    create_buttons(start_game_actions(), button_frame)
    window.mainloop()


def start_game_actions():
    """Restituisce le azioni possibili nella schermata di inizio gioco."""
    actions = [
        {"text": translations["class_selection"][lang], "callback": class_caller},
        {"text": translations["quit_game"][lang], "callback": end_game}
    ]
    return actions


def class_caller():
    create_buttons(class_actions(), button_frame)


def class_actions():
    actions = [
        {"text": translations["warrior"][lang], "callback": pg.warrior},
        {"text": translations["mage"][lang], "callback": pg.mage}
    ]
    return actions


def end_game():
    window.destroy()

