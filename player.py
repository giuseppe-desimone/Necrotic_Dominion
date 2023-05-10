from lv_1 import callbacks_l1 as c
class Player:
    def __init__(self, PV, PF, PM, g, inventory=None):
        self.PV = PV
        self.PF = PF
        self.PM = PM
        self.g = g
        if inventory is None:
            inventory = []
        self.inventory = inventory


PG = Player(PV=0, PF=0, PM=0, g=0, inventory=[])
oldguard = Player(PV=0, PF=0, PM=0, g=0, inventory=[])


def warrior():
    new_player(2)
    c.go_04()

def mage():
    new_player(1)
    c.go_04()


def new_player(type):

    if type == 2:
        PG.g = 0
        PG.PV = 20
        PG.PF = 3
        PG.PM = 0
        PG.inventory = []
    else:
        PG.g = 0
        PG.PV = 15
        PG.PF = 1
        PG.PM = 4
        PG.inventory = []

    oldguard.g = 0
    oldguard.PV = 17
    oldguard.PF = 4
    oldguard.PM = 0
    oldguard.inventory = []

def edit_stats(t, bonus):
    if t == 'M':
        PG.PM = PG.PM + bonus
    if t == 'F':
        PG.PF = PG.PF + bonus