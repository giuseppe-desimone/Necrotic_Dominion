"""v0.12"""

from interface import *
from lv_1 import callbacks_l1 as c
from lv_1 import map_l1
import random

perry = False

global p, e


def combat(pgplayer, pgenemy, previous_room, current_room):
    global p, e
    previous_room = previous_room
    current_room = current_room
    p = pgplayer
    e = pgenemy

    if p.PV > 0:
        if e.PV <= 0:
            getattr(c, f"go_{current_room:02d}")()
        else:
            i.create_buttons(combat_actions(previous_room, current_room))
    else:
        i.show_text("\n\n"+interface_translations["quit_game"][i.lang]+" Game over.")
        i.create_buttons(combat_actions(previous_room, current_room))


def combat_actions(previous_room, current_room):
    if p.PV <= 0:
        actions = [
            {"text": interface_translations["new_game"][i.lang], "callback": i.new_play},
            {"text": interface_translations["quit_game"][i.lang], "callback": i.end_game}
        ]
    else:
        actions = [
            {"text": interface_translations["flee"][i.lang], "callback": lambda: getattr(c, f"go_{previous_room:02d}")()},
            {"text": interface_translations["parry"][i.lang], "callback": lambda: para(previous_room, current_room)},
            {"text": interface_translations["arcane_missile"][i.lang], "callback": lambda: attacca(previous_room, current_room)}
        ]
        if p.PM >= 2:
            actions.append({"text": interface_translations["quit_game"][i.lang], "callback": lambda: invoke_missile(previous_room, current_room)})
    return actions


def invoke_missile(previous_room, current_room):
    p.PM -= 1
    damage = roll_dice(1, 6) + 7
    e.PV -= damage

    room_description = get_room_description(current_room)
    i.show_text(
        room_description + "\n\n---------------------------------\n\n"+ interface_translations["enemy_life"][i.lang] + str(e.PV)
                         + "\n\n---------------------------------"
                         + oldcombat_translations["missile_hit"][i.lang] + str(damage) + interface_translations["damage"][i.lang])
    combat(p, e, previous_room, current_room)


def para(previous_room, current_room):
    global perry
    perry = True  # reset the perry flag
    roll = roll_dice(1, 6)  # roll a 6-sided dice

    room_description = get_room_description(current_room)

    if roll in (1, 2):
        damage = roll_dice(1, 6) + e.PF  # add enemy's attack bonus
        p.PV -= damage
        i.show_text(
            room_description + "\n\n---------------------------------\n\n" + interface_translations["enemy_life"][i.lang] + str(e.PV)
                             +  "\n\n---------------------------------"
                             + oldcombat_translations["parry_miss"][i.lang] + str(damage) + interface_translations["damage"][i.lang])
    else:
        i.show_text(room_description + "\n\n---------------------------------\n\n"+ interface_translations["enemy_life"][i.lang] + str(e.PV)
                                     + "\n\n---------------------------------"
                                     + oldcombat_translations["parry_succ"][i.lang])

    combat(p, e, previous_room, current_room)


def attacca(previous_room, current_room):
    global p, e, perry
    room_description = get_room_description(current_room)

    if not perry:
        roll = roll_dice(1, 6)
        damage_e = roll + e.PF
        damage_p = roll + p.PF
        p.PV -= damage_e
        e.PV -= damage_p
        i.show_text(room_description + "\n\n---------------------------------\n\n"+ interface_translations["enemy_life"][i.lang] + str(e.PV)
                                     + "\n\n---------------------------------"
                    + oldcombat_translations["attack_received"][i.lang] + str(damage_e) + interface_translations["damage"][i.lang]
                    + "\n\n---------------------------------"
                    + oldcombat_translations["attack_done"][i.lang] + str(damage_p) + interface_translations["damage"][i.lang])
        combat(p, e, previous_room, current_room)
    else:
        roll = roll_dice(1, 6)  # roll a 6-sided dice
        damage = roll + p.PF  # add enemy's attack bonus
        e.PV -= damage
        i.show_text(room_description + "\n\n---------------------------------\n\n"+ interface_translations["enemy_life"][i.lang] + str(e.PV)
                                     + "\n\n---------------------------------"
                    + oldcombat_translations["attack_done"][i.lang] + str(damage) + interface_translations["damage"][i.lang])
        perry = False
        combat(p, e, previous_room, current_room)


def get_room_description(room_number):
    room_object = getattr(map_l1, f"s{room_number:02d}")
    return room_object.description


def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return sum(rolls)
