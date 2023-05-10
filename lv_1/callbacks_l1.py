"""v0.12"""

import interface as i
import combat_system as cs
from lv_1 import map_l1
from lv_1 import actions_l1 as a
from lv_1 import dialogs_l1 as d
import player as pg

v05 = False
v06 = False
v25 = False

############################################MOVIMENTI###################################################################


def go_03():
    """Muove il giocatore nella stanza 0,3."""
    i.image_wand("./lv_1/img/03")
    i.show_text(map_l1.s03.description)
    i.create_buttons(a.s03_actions(), i.button_frame)


def go_04():
    """Muove il giocatore nella stanza 0,4."""
    i.image_wand("./lv_1/img/04")
    i.show_text(map_l1.s04.description)
    i.create_buttons(a.s04_actions(), i.button_frame)


def go_05():
    """Muove il giocatore nella stanza 0,5."""
    i.image_wand("./lv_1/img/05")
    i.show_text(map_l1.s05.description)
    i.create_buttons(a.s05_actions(), i.button_frame)

def go_06():
    """Muove il giocatore nella stanza 0,6."""
    i.image_wand("./lv_1/img/06")
    i.show_text(map_l1.s06.description)
    i.create_buttons(a.s06_actions(), i.button_frame)


def go_14():
    """Muove il giocatore nella stanza 1,4."""
    i.image_wand("./lv_1/img/14")
    i.show_text(map_l1.s14.description)
    i.create_buttons(a.s14_actions(), i.button_frame)


def go_24():
    """Muove il giocatore nella stanza 2,4."""
    i.image_wand("./lv_1/img/24")
    i.show_text(map_l1.s24.description)
    i.create_buttons(a.s24_actions(), i.button_frame)


def go_25():
    """Muove il giocatore nella stanza 2,5."""
    if v25 is True:
        if pg.oldguard.PV > 0:
            i.show_text(map_l1.s25.description + "\n\n---------------------------------\n\nLa guardia se ne sta a terra, su quello che sembra un letto fatto di paglia, e sembra dormire.")
            i.create_buttons(a.s25_actions(), i.button_frame)
        else:
            i.show_text(map_l1.s25.description +"\n\n---------------------------------\n\nla guardia giace a terra, in una pozza di sangue.")
            i.create_buttons(a.s25_actions(), i.button_frame)
    else:
        if pg.oldguard.PV > 0:
            i.show_text(map_l1.s25.description +"\n\n---------------------------------\n\nC'è una vecchia guardia poggiata al tavolo, si gira e ti osserva con occhi spalancati.")
            i.create_buttons(a.s25_actions(), i.button_frame)
        else:
            i.show_text(map_l1.s25.description +"\n\n---------------------------------\n\nla guardia giace a terra, in una pozza di sangue. Sembra che abbia con se degli oggetti.")
            i.create_buttons(a.s25_actions(), i.button_frame)


##############################################AZIONI####################################################################

def drink_06():
    """Beve alla fontana"""
    global v06
    v06 = True
    pg.edit_stats('M', 2)
    i.show_text(map_l1.s06.description +"\n\n---------------------------------\n\nSenti la forte energia di centinaia di anime che ti permea. (Man. +2)")
    i.create_buttons(a.s06_actions(), i.button_frame)


def open_chest_with_key():
    """Apre la cassapanca con la chiave."""
    pg.PG.inventory.remove("chiave")
    pg.PG.inventory.append("spada")
    pg.edit_stats('F', 2)
    i.show_text(map_l1.s03.description +"\n\n---------------------------------\n\nHai recuperato una spada d'acciaio di squisita fattura. (For. +2)")
    i.create_buttons(a.s03_actions(), i.button_frame)


def open_door_05():
    global v05
    if 'chiave2' in pg.PG.inventory:
        v05 = True
        pg.PG.inventory.remove('chiave2')
        i.show_text(map_l1.s05.description +"\n\n---------------------------------\n\nHai aperto la porta.")
        i.create_buttons(a.s05_actions(), i.button_frame)
    else:
        i.show_text(map_l1.s05.description +"\n\n---------------------------------\n\nNon hai la chiave.")
        i.create_buttons(a.s05_actions(), i.button_frame)


def open_door_nokey_24():
    i.show_text(map_l1.s24.description + "\n\n---------------------------------\n\nNon hai la chiave.")
    i.create_buttons(a.s24_actions(), i.button_frame)


def pick_up_key():
    """Raccoglie la chiave."""
    pg.PG.inventory.append("chiave")
    i.show_text(map_l1.s04.description + "\n\n---------------------------------\n\nHai raccolto la chiave.")
    i.create_buttons(a.s04_actions(), i.button_frame)


def pick_up_key2():
    """Raccoglie la chiave2."""
    global v25
    v25 = True
    pg.PG.inventory.append("chiave2")
    if pg.oldguard.PV <= 0:
        i.show_text(map_l1.s25.description + "\n\n---------------------------------\n\nHai raccolto la chiave dal cadavere a terra.")
    else:
        i.show_text(
            map_l1.s25.description + "\n\n---------------------------------\n\nHai raccolto la chiave.\n\n---------------------------------\n\nLa guardia si sdraia a terra, su quello che sembra un letto fatto di paglia, \ne cerca di addormentarsi.")
    i.create_buttons(a.s25_actions(), i.button_frame)


############################################DIALOGHI####################################################################


def dialog_25_start():
    """Parlare con guardia in 25"""
    i.show_text(map_l1.s25.description + "\n\n---------------------------------\n\n'CHI SIETE!?' grida la guardia, con voce ferma.")
    i.create_buttons(d.s25_dialog_0(), i.button_frame)


def dialog_25_1():
    """Parlare con guardia in 25"""
    i.show_text(map_l1.s25.description + "\n\n---------------------------------\n\n'Neanche io...' sussurra la vecchia guardia, con voce rassegnata.\n'Che vuoi!?' esclama con follia.")
    i.create_buttons(d.s25_dialog_1(), i.button_frame)


def dialog_25_2():
    """Parlare con guardia in 25"""
    i.show_text(map_l1.s25.description + "\n\n---------------------------------\n\nLa vecchia guardia scoppia a ridere.\n'Non c'è via d'uscita! Questo posto è sigillato da un'antica magia'.\n'Prendi questa chiave, forse tornerà più utile a te che a me.'\n\n---------------------------------\n\nTi porge la chiave.")
    i.create_buttons(d.s25_dialog_2(), i.button_frame)


def dialog_25_kill():
    """Parlare con guardia in 25"""
    pg.oldguard.PV = 0
    i.show_text(map_l1.s25.description +"\n\n---------------------------------\n\nLa vecchia guardia ti scruta con occhi di incredula gratitudine.\n\n'Grazie', esala dalla bocca.")
    i.create_buttons(a.s25_actions(), i.button_frame)


def dialog_25_combat():
    """Parlare con guardia in 25"""
    i.show_text(map_l1.s25.description + "\n\n---------------------------------"
                                       + "\n\nVita del nemico: {} ".format(pg.oldguard.PV)
                                       + "\n\n---------------------------------"              
                                         "\n\n'QUESTO NON E' UN POSTO PER GIROVAGARE' \n\nil vecchio si alza e agita un bastone verso di te.")
    cs.combat(pg.PG, pg.oldguard, 24, 25)
