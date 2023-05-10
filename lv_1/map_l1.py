"""v0.12"""


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

mappa_l1[0][2].description
mappa_l1[0][3].description = "Nel cuore del castello si trova l’armeria, una vasta stanza dalle pareti in pietra ornate da \nantichi stemmi e scudi impolverati. \n\nUna volta custode di migliaia di armi e armature, ora le grandi mensole e gli armadi dell’armeria \nrimangono vuoti e silenziosi. \n\nUn’indicibile tristezza si respira nell’aria, interrotta solo dalla vista di una cassapanca in un \nangolo."
mappa_l1[0][4].description = "L’atrio del castello è spazioso, \ncon alti soffitti affrescati e \npareti di pietra che riflettono\nla luce. \n\nL’odore di fumo delle torce e di \ncera delle candele riempie \nl’aria, mentre i passi echeggiano \nsui pavimenti di marmo scuro. \n\nAi lati dell’atrio si trovano \ngrandi porte di quercia scolpite \na mano, una rivolta verso est e \nl’altra verso ovest. \n\nUn ampio corridoio si apre verso \nsud, con i lampadari appesi alle \npareti di pietra che illuminano \nil percorso e creano ombre \ndanzanti."
mappa_l1[0][5].description = "Ti trovi in una stanza vuota e desolata, senza finestre né mobili. \n\nLa tua unica via di uscita è una porta a ovest, mentre a est c'è una serratura. \n\nL'aria è silenziosa e immobile, creando un'atmosfera inquietante e misteriosa."
mappa_l1[0][6].description = "Al centro del salone buio si trova la fontana sacra, che emana una flebile luce blu e si avvolge in una foschia misteriosa. \n\nL'acqua che sgorga da essa è corrotta dalle anime dei sacrifici e nutre antiche divinità oscure, \noffrendo un potere oltre la comprensione umana a coloro che osano avvicinarsi."
mappa_l1[1][2].description
mappa_l1[1][4].description = "Ti trovi in un sontuoso corridoio dal pavimento di marmo, illuminato da lampadari pendenti. \n\nSulle pareti si trovano quadri di uomini dall'espressione severa che sembrano scrutarti. \n\nL'atmosfera è solenne e formale, \nma anche un po' intimidatoria. \n\nIl corridoio sembra non avere fine e non si vedono porte né finestre, come se fosse un labirinto senza\nvia d'uscita."
mappa_l1[2][2].description
mappa_l1[2][4].description = "Hai raggiunto la fine del corrido-io, dove trovi due porte. \n\nUna porta chiusa si trova a sud, \nsenza alcuna indicazione su cosa \npossa trovarsi dall'altra parte. \n\nLa seconda porta è ad est e non si può vedere attraverso la \nserratura. \n\nL'atmosfera è ancora solenne e \nmisteriosa, lasciando intendere che \nci possano essere segreti o \npericoli in agguato oltre le \nporte."
mappa_l1[2][5].description = "Entri in una stanza del castello \natipica. Sembra che sia stata \nriadattata a rifugio, con un \ngiaciglio per dormire, e un \nsemplice tavolo in legno. Una \ncandela accesa sul tavolo rompe \nil buio della stanza."
mappa_l1[3][2].description
mappa_l1[3][3].description
mappa_l1[3][4].description
mappa_l1[3][5].description

########################################################################################################################

mappa_l1[0][4].objects = ["chiave"]

########################################################################################################################

s02 = mappa_l1[0][2]
s03 = mappa_l1[0][3]
s04 = mappa_l1[0][4]
s05 = mappa_l1[0][5]
s06 = mappa_l1[0][6]
s12 = mappa_l1[1][2]
s14 = mappa_l1[1][4]
s22 = mappa_l1[2][2]
s24 = mappa_l1[2][4]
s25 = mappa_l1[2][5]
s32 = mappa_l1[3][2]
s33 = mappa_l1[3][3]
s34 = mappa_l1[3][4]
s35 = mappa_l1[3][5]