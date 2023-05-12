"""v0.12"""
from interface import *

class Stanza:
    def __init__(self, X, Y, description, objects=None):
        self.X = X
        self.Y = Y
        self.description = description
        if objects is None:
            objects = []
        self.objects = objects


# Creazione della matrice "mappa"
mappa_l1 = [[Stanza(X=i, Y=j, description="descrizione", objects=[]) for j in range(9)] for i in range(9)]


# Aggiunta di alcune stanze alla mappa

mappa_l1[0][3].description = translations["l1_03"][i.lang]
mappa_l1[0][4].description = translations["l1_04"][i.lang]
mappa_l1[0][5].description = translations["l1_05"][i.lang]
mappa_l1[0][6].description = translations["l1_06"][i.lang]
mappa_l1[1][4].description = translations["l1_14"][i.lang]
mappa_l1[2][4].description = translations["l1_24"][i.lang]
mappa_l1[2][5].description = translations["l1_25"][i.lang]
mappa_l1[3][4].description = translations["l1_34"][i.lang]

########################################################################################################################

mappa_l1[0][4].objects = ["chiave"]

########################################################################################################################


s03 = mappa_l1[0][3] # armeria
s04 = mappa_l1[0][4] # atrio
s05 = mappa_l1[0][5] # stanza vuota
s06 = mappa_l1[0][6] # fontana
s14 = mappa_l1[1][4] # corridoio
s24 = mappa_l1[2][4] # fine corridoio
s25 = mappa_l1[2][5] # rifugio guardia
s34 = mappa_l1[3][4] # scale

