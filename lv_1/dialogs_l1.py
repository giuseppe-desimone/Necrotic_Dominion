from lv_1 import callbacks_l1 as c
from lv_1 import actions_l1 as a

def s25_dialog_0():
    """Restituisce le azioni possibili nella stanza 2,5."""
    actions = [
        {"text": "... non rispondere ...", "callback": c.dialog_25_combat},
        {"text": "'non mi ricordo come sono finito quì'", "callback": c.dialog_25_1}
    ]
    return actions

def s25_dialog_1():
    """Restituisce le azioni possibili nella stanza 2,5."""
    actions = [
        {"text": "... non rispondere ...", "callback": c.dialog_25_combat},
        {"text": "'Come esco da qui?'", "callback": c.dialog_25_2}
    ]
    return actions

def s25_dialog_2():
    """Restituisce le azioni possibili nella stanza 2,5."""
    actions = [
        {"text": "Prendi la chiave", "callback": c.pick_up_key2}
    ]
    return actions