"""v0.12"""

import os
import sys

from interface import *

from interactions import combat_system as cs
from lv_1 import map_l1
from lv_1 import actions_l1 as a
from lv_1 import dialogs_l1 as d
import player as pg

v05 = False # porta stanza chiusa/apertta
v06 = False # bevutto alla fontana
v06a = False # raccolta chiave imp
v25 = False # chiave guardia
v24 = False # porta aperta / chiusa

############################################MOVIMENTI###################################################################

def go_03():
    """Muove il giocatore nella stanza 0,3."""
    i.image_wand("./media/img_lv1/03")
    i.show_text(map_l1.s03.description)
    i.create_buttons(a.s03_actions())


def go_04():
    """Muove il giocatore nella stanza 0,4."""
    i.image_wand("./media/img_lv1/04")
    i.show_text(map_l1.s04.description)
    i.create_buttons(a.s04_actions())


def go_05():
    """Muove il giocatore nella stanza 0,5."""
    i.image_wand("./media/img_lv1/05")
    i.show_text(map_l1.s05.description)
    i.create_buttons(a.s05_actions())

def go_06():
    """Muove il giocatore nella stanza 0,6."""
    i.image_wand("./media/img_lv1/06")
    if pg.l1_imp.PV > 0:
        i.show_text(map_l1.s06.description+ callbacks_translations["l1_st06fight"][i.lang])
        i.create_buttons(a.s06_actions())
    else: 
        i.show_text(map_l1.s06.description+ callbacks_translations["l1_rs06fight"][i.lang])
        i.create_buttons(a.s06_actions())


def go_14():
    """Muove il giocatore nella stanza 1,4."""
    i.image_wand("./media/img_lv1/14")
    i.show_text(map_l1.s14.description)
    i.create_buttons(a.s14_actions())


def go_24():
    """Muove il giocatore nella stanza 2,4."""
    i.image_wand("./media/img_lv1/24")
    i.show_text(map_l1.s24.description)
    i.create_buttons(a.s24_actions())


def go_25():
    """Muove il giocatore nella stanza 2,5."""
    if v25 is True:
        if pg.l1_oldguard.PV > 0:
            i.image_wand("./media/img_lv1/25r")
            i.show_text(map_l1.s25.description + callbacks_translations["l1_25sleep"][i.lang])
            i.create_buttons(a.s25_actions())
        else:
            i.image_wand("./media/img_lv1/25r")
            i.show_text(map_l1.s25.description + callbacks_translations["l1_25dead-taken"][i.lang])
            i.create_buttons(a.s25_actions())
    else:
        i.image_wand("./media/img_lv1/25")
        if pg.l1_oldguard.PV > 0:
            i.show_text(map_l1.s25.description + callbacks_translations["l1_25encounter"][i.lang])
            i.create_buttons(a.s25_actions())
        else:
            i.image_wand("./media/img_lv1/25r")
            i.show_text(map_l1.s25.description + callbacks_translations["l1_25dead-items"][i.lang])
            i.create_buttons(a.s25_actions())


def go_34():
    """Muove il giocatore nella stanza 3,4."""
    if pg.l1_undead.PV > 0:
        i.image_wand("./media/img_lv1/34")
        i.show_text(map_l1.s34.description + callbacks_translations["l1_34fight"][i.lang])
    else:
        i.image_wand("./media/img_lv1/34r")
        i.show_text(map_l1.s34.description + callbacks_translations["l1_34dead"][i.lang])
    
    i.create_buttons(a.s34_actions())


##############################################AZIONI####################################################################

def drink_06():
    """Beve alla fontana"""
    global v06
    v06 = True
    pg.edit_stats('M', 2)
    i.show_text(map_l1.s06.description + callbacks_translations["l1_r06drink"][i.lang])
    i.create_buttons(a.s06_actions())


def open_chest_with_key():
    """Apre la cassapanca con la chiave."""
    pg.PG.inventory.remove("chiave")
    pg.PG.inventory.append("spada")
    pg.edit_stats('F', 2)
    i.show_text(map_l1.s03.description + callbacks_translations["l1_03sword"][i.lang])
    i.create_buttons(a.s03_actions())


def open_door_05():
    global v05
    if 'chiave2' in pg.PG.inventory:
        v05 = True
        pg.PG.inventory.remove('chiave2')
        i.show_text(map_l1.s05.description + callbacks_translations["l1_nokey"][i.lang])
        i.create_buttons(a.s05_actions())
    else:
        i.show_text(map_l1.s05.description + callbacks_translations["l1_nokey"][i.lang])
        i.create_buttons(a.s05_actions())


def open_door_nokey_24():
    i.show_text(map_l1.s24.description + callbacks_translations["l1_nokey"][i.lang])
    i.create_buttons(a.s24_actions())

def open_door_24():
    global v24
    if 'chiave3' in pg.PG.inventory:
        v24 = True
        pg.PG.inventory.remove('chiave3')
        i.show_text(map_l1.s24.description + callbacks_translations["l1_nokey"][i.lang])
        i.create_buttons(a.s24_actions())
    else:
        i.show_text(map_l1.s24.description + callbacks_translations["l1_nokey"][i.lang])
        i.create_buttons(a.s24_actions())

def pick_up_key():
    """Raccoglie la chiave."""
    pg.PG.inventory.append("chiave")
    i.show_text(map_l1.s04.description + callbacks_translations["l1_pickupkey"][i.lang])
    i.create_buttons(a.s04_actions())


def pick_up_key2():
    """Raccoglie la chiave2."""
    global v25
    v25 = True
    i.image_wand("./media/img_lv1/25r")
    pg.PG.inventory.append("chiave2")
    if pg.l1_oldguard.PV <= 0:
        i.show_text(map_l1.s25.description + callbacks_translations["l1_pickupkeydead"][i.lang])
    else:
        i.show_text(
            map_l1.s25.description +  callbacks_translations["l1_pickupkey"][i.lang] + callbacks_translations["l1_25gosleep"][i.lang] )
    i.create_buttons(a.s25_actions())


def pick_up_key3():
    """Raccoglie la chiave3."""
    global v06a
    v06a = True
    i.image_wand("./media/img_lv1/06")
    pg.PG.inventory.append("chiave3")
    i.show_text(map_l1.s06.description + callbacks_translations["l1_pickupkeyimp"][i.lang])
    i.create_buttons(a.s06_actions())


############################################COMBATTIMENTI####################################################################



def combat_06():
    """Combattere imp in 06"""
    i.show_text(map_l1.s06.description + "\n\n---------------------------------"
                                       + "\n\nVita del nemico: {} ".format(pg.l1_imp.PV)
                                       + "\n\n---------------------------------"              
                                         "\n\nL'Imp si avventa con voracità famelica in cerca della tua vita")
    cs.combat(pg.PG, pg.l1_imp,5,6)


def dialog_25_combat():
    """Parlare con guardia in 25"""
    i.show_text(map_l1.s25.description + "\n\n---------------------------------"
                                       + "\n\nVita del nemico: {} ".format(pg.l1_oldguard.PV)
                                       + "\n\n---------------------------------"              
                                         "\n\n'QUESTO NON E' UN POSTO PER GIROVAGARE' \n\nil vecchio si alza e agita un bastone verso di te.")
    cs.combat(pg.PG, pg.l1_oldguard, 24, 25)

def combat_34():
    """Combattere imp in 34"""
    i.show_text(map_l1.s34.description + "\n\n---------------------------------"
                                       + "\n\nVita del nemico: {} ".format(pg.l1_undead.PV)
                                       + "\n\n---------------------------------"              
                                         "\n\nIl non morto ti attacca per scopartti nel culo")
    cs.combat(pg.PG, pg.l1_undead,24,34)

############################################DIALOGHI####################################################################


def dialog_25_start():
    """Parlare con guardia in 25"""
    i.show_text(map_l1.s25.description + "\n\n---------------------------------\n\n'CHI SIETE!?' grida la guardia, con voce ferma.")
    i.create_buttons(d.s25_dialog_0())


def dialog_25_1():
    """Parlare con guardia in 25"""
    i.show_text(map_l1.s25.description + "\n\n---------------------------------\n\n'Neanche io...' sussurra la vecchia guardia, con voce rassegnata.\n'Che vuoi!?' esclama con follia.")
    i.create_buttons(d.s25_dialog_1())


def dialog_25_2():
    """Parlare con guardia in 25"""
    i.show_text(map_l1.s25.description + "\n\n---------------------------------\n\nLa vecchia guardia scoppia a ridere.\n'Non c'è via d'uscita! Questo posto è sigillato da un'antica magia'.\n'Prendi questa chiave, forse tornerà più utile a te che a me.'\n\n---------------------------------\n\nTi porge la chiave.")
    i.create_buttons(d.s25_dialog_2())


def dialog_25_kill():
    """Parlare con guardia in 25"""
    pg.l1_oldguard.PV = 0
    i.show_text(map_l1.s25.description +"\n\n---------------------------------\n\nLa vecchia guardia ti scruta con occhi di incredula gratitudine.\n\n'Grazie', esala dalla bocca.")
    i.create_buttons(a.s25_actions())
