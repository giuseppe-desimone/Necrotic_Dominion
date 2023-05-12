
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from components import *
import player as pg
from interface import *

def setup_level_2(i):
    matrix_l2 = [[Room(X=i, Y=j) for j in range(9)] for i in range(9)]

    matrix_l2[0][4].description = "L’atrio del castello è spazioso, \ncon alti soffitti affrescati e \npareti di pietra che riflettono\nla luce. \n\nL’odore di fumo delle torce e di \ncera delle candele riempie \nl’aria, mentre i passi echeggiano \nsui pavimenti di marmo scuro. \n\nAi lati dell’atrio si trovano \ngrandi porte di quercia scolpite \na mano, una rivolta verso est e \nl’altra verso ovest. \n\nUn ampio corridoio si apre verso \nsud, con i lampadari appesi alle \npareti di pietra che illuminano \nil percorso e creano ombre \ndanzanti."
    matrix_l2[0][4].img = "./media/img_lv1/04"
    matrix_l2[0][4].item = Item("key0").action("Raccogli la chiave", pg.PG.item_pickup, "key0", repeat=False, matrix=matrix_l2, room=(0, 4))
    matrix_l2[0][4].action(
        "Vai ad est",
        matrix_l2[0][3].render, i,
        matrix=matrix_l2,
        room=(0, 3)
    )

    matrix_l2[0][3].description = "Nel cuore del castello si trova l’armeria, una vasta stanza dalle pareti in pietra ornate da \nantichi stemmi e scudi impolverati. \n\nUna volta custode di migliaia di armi e armature, ora le grandi mensole e gli armadi dell’armeria \nrimangono vuoti e silenziosi. \n\nUn’indicibile tristezza si respira nell’aria, interrotta solo dalla vista di una cassapanca in un \nangolo."
    matrix_l2[0][3].img = "./media/img_lv1/03"
    matrix_l2[0][3].action(
        "Vai a ovest",
        matrix_l2[0][4].render, i,
        matrix=matrix_l2,
        room=(0, 4)
    )

    return matrix_l2


def level_2(i):
    matrix_l2 = setup_level_2(i)
    matrix_l2[0][4].render(i)
