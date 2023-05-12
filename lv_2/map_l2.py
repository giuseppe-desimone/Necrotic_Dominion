
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from components import *
from interface import *

def setup_level_2():
    matrix_l2 = [[Room(X=i, Y=j) for j in range(9)] for i in range(9)]

    matrix_l2[4][4].description = translations["l2_44"][i.lang]
    matrix_l2[4][4].img = "./media/img_lv2/44"
    matrix_l2[4][4].item = Item("key0").action("Raccogli la chiave", pg.PG.item_pickup, "key0", repeat=False, matrix=matrix_l2, room=(4, 4))
    matrix_l2[4][4].action(
        "Vai ad est",
        matrix_l2[3][5].render,
        matrix=matrix_l2,
        room=(3, 5)
    )

    matrix_l2[3][5].description = translations["l2_35"][i.lang]
    matrix_l2[3][5].img = "./media/img_lv2/35"
    matrix_l2[3][5].action(
        "Torna nella grande sala",
        matrix_l2[4][4].render,
        matrix=matrix_l2,
        room=(4, 4)
    )

    return matrix_l2


def level_2():
    matrix_l2 = setup_level_2()
    matrix_l2[4][4].render()
