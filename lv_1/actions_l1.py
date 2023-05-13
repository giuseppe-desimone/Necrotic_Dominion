"""v0.13"""

import player as pg
from lv_1 import callbacks_l1 as c
from lv_2.map_l2 import *

def s03_actions():
    """Restituisce le azioni possibili nella stanza 0,3."""
    actions = [
        {"text": actions_translations["back-east"][i.lang], "callback": c.go_04}
    ]
    if "chiave" in pg.PG.inventory:
        actions.append({"text": actions_translations["open-chest"][i.lang], "callback": c.open_chest_with_key})
    return actions


def s04_actions():
    """Restituisce le azioni possibili nella stanza iniziale."""
    if 'chiave' in pg.PG.inventory or 'spada' in pg.PG.inventory:
        actions = [
            {"text":  actions_translations["go-east"][i.lang], "callback": c.go_05},
            {"text":  actions_translations["go-west"][i.lang], "callback": c.go_03},
            {"text":  actions_translations["l1_04-14"][i.lang], "callback": c.go_14}
        ]
    else:
        actions = [
            {"text":  actions_translations["go-east"][i.lang], "callback": c.go_05},
            {"text":  actions_translations["go-west"][i.lang], "callback": c.go_03},
            {"text":  actions_translations["l1_04-14"][i.lang], "callback": c.go_14},
            {"text":  actions_translations["pickup-key"][i.lang], "callback": c.pick_up_key}
        ]
    return actions

def s05_actions():
    """Restituisce le azioni possibili nella stanza 0,5."""
    if c.v05 is True:
        actions = [
            {"text": actions_translations["go-west"][i.lang], "callback": c.go_04},
            {"text": actions_translations["l1_05-06"][i.lang], "callback": c.go_06}
        ]
    else:
        actions = [
            {"text": actions_translations["l1_05-04"][i.lang], "callback": c.go_04},
            {"text": actions_translations["open-door"][i.lang], "callback": c.open_door_05}
        ]
    return actions


def s06_actions():
    if pg.l1_imp.PV > 0:
            actions = [
                    {"text": actions_translations["06attack"][i.lang], "callback": c.combat_06},
                    # {"text": "Vai ad ovest verso la stanza vuota", "callback": c.go_05}
                ]
    else:
        actions = []
        actions.append({"text": actions_translations["l1_06-05"][i.lang], "callback": c.go_05})
        
        if c.v06a is False:
                actions.append({"text": actions_translations["06pickup"][i.lang], "callback": c.pick_up_key3})
        if c.v06 is False:
                actions.append({"text": actions_translations["06drink"][i.lang], "callback": c.drink_06})

    return actions


def s14_actions():
    """Restituisce le azioni possibili nella stanza 1,4."""
    actions = [
        {"text": actions_translations["l1_14-04"][i.lang], "callback": c.go_04},
        {"text": actions_translations["l1_14-24"][i.lang], "callback": c.go_24}

    ]
    return actions


def s24_actions():
    """Restituisce le azioni possibili nella stanza 2,4."""
    if c.v06a is True:
        if c.v24 is False:
            actions = [
                {"text": actions_translations["l1_24-14"][i.lang], "callback": c.go_14},
                {"text": actions_translations["open-door-south"][i.lang], "callback": c.open_door_24},
                {"text": actions_translations["open-door-east"][i.lang], "callback": c.go_25}
            ]
        else:
            actions = [
                {"text": actions_translations["l1_24-14"][i.lang], "callback": c.go_14},
                {"text": actions_translations["enter-door-south"][i.lang], "callback": c.go_34},
                {"text": actions_translations["open-door-east"][i.lang], "callback": c.go_25}
            ]
    else:
        actions = [
            {"text": actions_translations["l1_24-14"][i.lang], "callback": c.go_14},
            {"text": actions_translations["open-door-south"][i.lang], "callback": c.open_door_nokey_24},
            {"text": actions_translations["open-door-east"][i.lang], "callback": c.go_25}
        ]
    return actions


def s25_actions():
    """Restituisce le azioni possibili nella stanza 2,5."""
    actions = [
        {"text": actions_translations["l1_25-24"][i.lang], "callback": c.go_24},
    ]
    if c.v25 is True:
        if pg.l1_oldguard.PV > 0:
            actions.append({"text": actions_translations["25kill"][i.lang], "callback": c.dialog_25_kill})
    else:
        if pg.l1_oldguard.PV > 0:
           
            actions.append({"text": actions_translations["25dialog"][i.lang], "callback": c.dialog_25_start})
            actions.append({"text": actions_translations["25attack"][i.lang], "callback": c.dialog_25_combat})
        else:
            actions.append({"text": actions_translations["25inspect"][i.lang], "callback": c.pick_up_key2})
    return actions


def s34_actions():
    """Restituisce le azioni possibili nella stanza 1,4."""
    if pg.l1_undead.PV > 0:
        actions = [
            {"text": actions_translations["34attack"][i.lang], "callback": c.combat_34},
            # {"text": "Vai ad ovest verso la stanza vuota", "callback": c.go_05}
        ]
    else:
        actions = [
            {"text": actions_translations["upstairs"][i.lang], "callback": level_2},
            {"text": actions_translations["go-back"][i.lang], "callback": c.go_24}
        ]

    return actions