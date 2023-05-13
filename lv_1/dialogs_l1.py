"""v0.13"""
########################################################################################################################
from lv_1 import callbacks_l1 as c
from interface import *

def s25_dialog_0():
    """Restituisce le azioni possibili nella stanza 2,5."""
    actions = [
        {"text": olddialog_transaltions["l1_25dont-reply"][i.lang], "callback": c.dialog_25_combat},
        {"text": olddialog_transaltions["l1_25dialog0"][i.lang], "callback": c.dialog_25_1}
    ]
    return actions


def s25_dialog_1():
    """Restituisce le azioni possibili nella stanza 2,5."""
    actions = [
        {"text": olddialog_transaltions["l1_25dont-reply"][i.lang], "callback": c.dialog_25_combat},
        {"text": olddialog_transaltions["l1_25dialog1"][i.lang], "callback": c.dialog_25_2}
    ]
    return actions


def s25_dialog_2():
    """Restituisce le azioni possibili nella stanza 2,5."""
    actions = [
        {"text": olddialog_transaltions["l1_25dialog2"][i.lang], "callback": c.pick_up_key2}
    ]
    return actions
