"""v0.12"""

from interface import *

class Player:
    def __init__(self, PV, PF, PM, g, inventory=None):
        self.PV = PV
        self.PF = PF
        self.PM = PM
        self.g = g
        if inventory is None:
            inventory = []
        self.inventory = inventory

        self.combat_actions = []

        # self.combat_actions.push(
        #     Action
        # )

    def item_pickup(self, itemid):
        self.inventory.append(itemid)


class Warrior(Player):
    def __init__(self, PV=0, PF=0, PM=0, g=0, inventory=None):
        super().__init__(PV,PF,PM,g)
        self.PV += 20
        self.PF += 3
        self.PM += 0
        self.g += 0
        global PG
        PG = self

class Mage(Player):
    def __init__(self, PV=0, PF=0, PM=0, g=0, inventory=None):
        super().__init__(PV,PF,PM,g)
        self.PV += 15
        self.PF += 1
        self.PM += 4
        self.g += 0
        global PG
        PG = self

class Oldguard(Player):
    def __init__(self, PV=0, PF=0, PM=0, g=0, inventory=None):
        super().__init__(PV,PF,PM,g)
        self.PV += 17
        self.PF += 5
        self.PM += 0
        self.g += 4

    def loot(self):
        return self.g


class IMP(Player):
    def __init__(self, PV=0, PF=0, PM=0, g=0, inventory=None):
        super().__init__(PV,PF,PM,g)
        self.PV += 10
        self.PF += 3
        self.PM += 0
        self.g += 0

    def loot(self):
        return self.g

class Zombie(Player):
    def __init__(self, PV=0, PF=0, PM=0, g=0, inventory=None):
        super().__init__(PV,PF,PM,g)
        self.PV += 5
        self.PF += 10
        self.PM += 0
        self.g += 0

    def loot(self):
        return self.g


def edit_stats(t, bonus):
    if t == 'M':
        PG.PM += bonus
    if t == 'F':
        PG.PF += bonus

PG = Player(PV=0, PF=0, PM=0, g=0, inventory=[])
l1_oldguard = Oldguard(PV=0, PF=0, PM=0, g=0, inventory=[])
l1_imp = IMP(PV=0, PF=0, PM=0, g=0, inventory=[])
l1_undead = Zombie(PV=0, PF=0, PM=0, g=0, inventory=[])


