"""v0.13"""

interface_translations = {# add arcane lang??
        "interface_life":       { "en": "Life",                         "it":"Vita" },
        "interface_strenght":   { "en": "Strenght",                     "it":"Forza" },
        "interface_mana":       { "en": "Mana",                         "it":"Mana" },
        "interface_gold":       { "en": "Gold",                         "it":"Oro" },
        "pg_invetory":          { "en": "Inventory",                    "it":"Inventario" },

        "class_selection" :     {"en":"Class Selection",                "it":"Selezione della classe"},
        "level_selection" :     {"en":"Level Selection",                "it":"Selezione del livello"},
        "lev_1" :               {"en":"Level 1",                        "it":"Livello 1"},
        "lev_2" :               {"en":"Level 2",                        "it":"Livello 2"},
        "new_game" :            {"en":"New Game",                       "it":"Nuova Partita"},
        "quit_game" :           {"en":"Quit",                           "it":"Chiudi il gioco"},

        "game_over" :           {"en":"You are dead",                   "it":"Sei morto"},
        
        "enemy_life" :          {"en":"Enemy Life:",                    "it":"Vita del nemico:"},
        "arcane_missile" :      {"en":"Summon an arcane missile",       "it":"Lancia un missile arcano"},
        "flee" :                {"en":"Flee",                           "it":"Scappa"},
        "parry" :               {"en":"Shield",                         "it":"Para"},
        "attack" :              {"en":"Attack",                         "it":"Attacca"},
        "damage" :              {"en":"Damage",                         "it":"Danni"},

        "warrior" :             {"en":"Skilled in combat",          "it":"Abile nel combattimento"},
        "mage" :                {"en":"Skilled in arcane arts",     "it":"Abile nelle arti arcane"},
}

oldcombat_translations = {
    "missile_hit" : {"it":"\n\nLa tua energia travolge l'avversario, arrecandogli ", "en":"\n\nYour energy overwhelms the opponent, causing "},
    "parry_miss" : {"it":"\n\nHai tentato di parare, ma hai subito ", "en":"\n\nYou attempted to parry, but you took "},
    "parry_succ" : {"it":"\n\nHai parato!", "en":"\n\nYou parry!"},
    "attack_received" : {"it":"\n\nVieni Attaccato, hai subito ", "en":"\n\nYou're Attacked, you've got "},
    "attack_done" : {"it":"\n\nColpo Sferrato, hai tolto ", "en":"\n\nStriked blow, you inflicted "},
}

olddialog_transaltions = {
    "l1_25dont-reply":{"it":"Non rispondere","en":"Do not reply"},
    "l1_25dialog0":{"it":"'Non ricordo come sono finito qui'","en":"'I don't remember how I ended here'"},
    "l1_25dialog1":{"it":"'Come esco da qui?'","en":"'How do I go out form this place?'"},
    "l1_25dialog2":{"it":"Prendi la chiave","en":"Take the key"},
}

level_translations = {
        "l1_03":                {"en":"In the heart of the castle lies \nthe armory, a vast chamber with \nstone walls adornedwith ancient \ncrests and dusty shields.\n\nOnce the guardian of thousands of weapons and armor, now the \ntowering shelves and armory \ncabinets remain empty and silent.\n\nAn indescribable sadness lingers \nin the air, only interrupted by \nthe sight of a chest in a \ncorner.",
                                 "it":"Nel cuore del castello si trova \nl’armeria, una vasta stanza dalle pareti in pietra ornate da \nantichi stemmi impolverati. \n\nUna volta custode di migliaia di \narmi e armature, ora le grandi \nmensole e gli armadi dell’armeria \nrimangono vuoti e silenziosi. \n\nUn’indicibile tristezza si respira nell’aria, interrotta solo dalla \nvista di una cassapanca in un \nangolo."},
        "l1_04":                {"en":"The castle's foyer is spacious,\nwith high frescoed ceilings and\nstone walls that reflect the \nlight.\n\nThe scent of torch smoke and\nwax candles fills the air,\nwhile footsteps echo on the dark\nmarble floors.\n\nOn either side of the foyer\nstand large oak doors, intricately\ncarved, one leading east\nand the other west.\n\nA wide corridor opens\nsouthward, with wall-mounted\nchandeliers illuminating the path\nand creating dancing shadows.",
                                 "it":"L’atrio del castello è spazioso, \ncon alti soffitti affrescati e \npareti di pietra che riflettono\nla luce. \n\nL’odore di fumo delle torce e di \ncera delle candele riempie \nl’aria, mentre i passi echeggiano \nsui pavimenti di marmo scuro. \n\nAi lati dell’atrio si trovano \ngrandi porte di quercia scolpite \na mano, una rivolta verso est e \nl’altra verso ovest. \n\nUn ampio corridoio si apre verso \nsud, con i lampadari appesi alle \npareti di pietra che illuminano \nil percorso e creano ombre \ndanzanti."},
        "l1_05":                {"en":"You find yourself in an empty and\ndesolate room, devoid of furniture\nor lights. \n\nYour only way out is a\ndoor to the west, while to the \neast there is a lock. \n\nThe air is silentand still, \ncreating an eerie and\nmysterious atmosphere.",
                                 "it":"Ti trovi in una stanza vuota e \ndesolata, senza mobili o luci. \n\nLa tua unica via di uscita è una \nporta a ovest, mentre a est c'è \nuna serratura. \n\nL'aria è silenziosa e immobile, \ncreando un'atmosfera inquietante e \nmisteriosa."},
        "l1_06":                {"en":"At the center of the dark hall, \nthere lies the sacred fountain, \nemitting a faint blue light \nand shrouded in mysterious mist. \n\nThe water that flows from it \nis tainted by the souls of \nsacrifices, nourishing ancient \ndark deities and bestowing \na power beyond human \ncomprehension upon those \nwho dare to approach.",
                                 "it":"Al centro del salone buio si \ntrova la fontana sacra, che \nemana una flebile luce \nblu e si avvolge in una \nfoschia misteriosa. \n\nL'acqua che sgorga da \nessa è corrotta dalle anime \ndei sacrifici e nutre \nantiche divinità oscure, \noffrendo un potere oltre \nla comprensione umana a \ncoloro che osano \navvicinarsi."},
        "l1_14":                {"en":"You find yourself in a lavish \ncorridor with a marble floor, il-\nluminated by hanging chandeliers. \n\nThe atmosphere is solemn and \nformal, but also somewhat \nintimidating. \n\nThe corridor seems to stretch \nendlessly, with no doors or \nwindows in sight, as if it were a labyrinth without an exit.",
                                 "it":"Ti trovi in un sontuoso corridoio dal pavimento di marmo, illuminato da lampadari pendenti. \n\nL'atmosfera è solenne e formale, \nma anche un po' intimidatoria. \n\nIl corridoio sembra non avere fine e non si vedono porte né finestre, come se fosse un labirinto senza\nvia d'uscita."},
        "l1_24":                {"en":"You have reached the end of the \ncorridor, where you find two \ndoors. \n\nA closed door is located to the \nsouth, without any indication of \nwhat might be on the other side. \n\nThe second door is to the east, \nand you cannot see through the \nkeyhole. \n\nThe atmosphere is still solemn and mysterious, suggesting that there may be secrets or dangers lurking beyond the doors.",
                                 "it":"Hai raggiunto la fine del corrido-io, dove trovi due porte. \n\nUna porta chiusa si trova a sud, \nsenza alcuna indicazione su cosa \npossa trovarsi dall'altra parte. \n\nLa seconda porta è ad est e non si può vedere attraverso la \nserratura. \n\nL'atmosfera è ancora solenne e \nmisteriosa, lasciando intendere \nche ci possano essere segreti o \npericoli in agguato oltre le \nporte."},
        "l1_25":                {"en":"You enter a nontraditional room \nin the castle. It seems to have \nbeen repurposed as a shelter, \nwith a makeshift sleeping pallet, \nand a simple wooden table. \nA lit candle on the table breaks \nthe darkness of the room.",
                                 "it":"Entri in una stanza del castello \natipica. Sembra che sia stata \nriadattata a rifugio, con un \ngiaciglio per dormire, e un \nsemplice tavolo in legno. Una \ncandela accesa sul tavolo rompe \nil buio della stanza."},
        "l1_34":                {"en":"You find yourself in a grand room\nwith a majestic staircase that \nascends upstairs. \nThe walls are adorned with \nenigmatic symbols, and dim lights\ncast eerie shadows. The air is \nfilled with a solemn and \nmysterious atmosphere that \npermeates the surroundings.",
                                 "it":"Ti trovi in una grande stanza\ncon una maestosa scala che si \ninnalza verso l'alto. \nLe pareti sono decorate con \nsimboli enigmatici e le luci \nfiocche gettano ombre inquietanti. \nL'aria è pregna di un'atmosfera \nsolenne e misteriosa che \npermea l'ambiente."},

        "l2_44":                {"en": "The hall of the castle stands \nmajestic, shrouded in the \nshadow of the past. Dark stone \nwalls rise with mastery, adorned \nwith intricate friezes and \nsinister images. Three identical \ndoors, intricately carved in \ngothic fashion, loom ominously. \nTheir dark wood seems to resonate \nwith ancient whispers and \nunutterable secrets. Each door \nconceals an uncertain destiny, \na path to revelation or \ndarkness. The atmosphere is \nthick with oppressive energy, \nwhile restless shadows dance \non the marble floor. A chilling \ncold envelops the air, carrying \nthe allure of unfathomable \nmysteries that lie beyond those doors.",
                                 "it": "Il salone del castello si erge \nmaestoso, avvolto dall'ombra \ndel passato. Pareti di pietra \nscura si ergono con maestria, \nornate da fregi intricati e \nimmagini sinistre. Tre porte \nidentiche, intagliate con \nraffinatezza gotica, si \nstagliano inquietanti. Il loro \nlegno scuro sembra risuonare \ndi antichi sussurri e segreti \ninconfessabili. Ogni porta cela \nun destino incerto, un cammino \nverso la rivelazione o \nl'oscurità. L'atmosfera è \npregnante di un'energia \noppressiva, mentre le ombre \ndanzano inquiete sul pavimento \ndi marmo. Un freddo gelido \navvolge l'aria, portando con \nsé il richiamo dei misteri \ninsondabili che si celano \noltre quelle porte."},
        "l2_35":                {"en": "The corridor stretches ahead,\na path of shadows in the heart of darkness.\nDark stone walls rise like silent guardians,\nwhile a faint moonlight filters through the windows.\nThe air is filled with a gloomy atmosphere,\ninfused with arcane presences.\nRestless shadows dance along the marble floor,\nenhancing the sense of mystery.\nEvery step echoes, accentuating the funereal silence.\nVenturing further means facing the unknown,\nuncovering dark truths and buried secrets.",
                                 "it": "Nel profondo della notte, lungo un \ncorridoio oscurato dall'ombra, si \nestende un tragitto proibito. \nI muri screpolati si ergono \nminacciosi mentre la luce delle \nfiaccole balbetta. \nLe pareti silenziose \ncustodiscono antichi segreti, e il \nsuono dei passi risuona in un eco \nsinistro mentre si avanza verso \nl'ignoto."}
}

objects_translations = {
    "key0" : {"it":"Noti una chiave arrugginita a terra", "en":"You see a rusty key on the ground"}
}

actions_translations = {
    "back-east":            {"it": "Torna a Est",                                       "en": "Go back to East"},
    "open-chest":           {"it": "Apri la cassapanca",                                "en": "Open chest"},
    "go-back":              {"it": "Torna indietro",                                    "en": "Go back"},
    "go-east":              {"it": "Vai a Est",                                         "en": "Go to East"},
    "go-west":              {"it": "Vai a Ovest",                                       "en": "Go to Ovest"},
    "pickup-key":           {"it": "Raccogli la chiave",                                "en": "Pick up the key"},
    "open-door":            {"it": "Apri la porta",                                     "en": "Open the door"},
    "open-door-east":       {"it": "Apri la porta ad Est",                              "en": "Open the East door"},
    "open-door-west":       {"it": "Apri la porta ad Ovest",                            "en": "Open the West door"},
    "open-door-south":      {"it": "Apri la porta a Sud",                               "en": "Open the South door"},
    "enter-door-east":      {"it": "Entra nela porta ad Est",                           "en": "Enter the East door"},
    "enter-door-south":     {"it": "Entra nela porta a Sud",                            "en": "Enter the South door"},
    "upstairs":             {"it": "Sali le scale",                                     "en": "Go up the stairs"},
    "l1_04-14":             {"it": "Vai a Sud in quello che sembra un corridoio buio",  "en": "Go South through a dark corridor"},
    "l1_05-06":             {"it": "Entra nella porta ad Est",                          "en": "Go back using the East door"},
    "l1_05-04":             {"it": "Vai ad Ovest nell'atrio",                           "en": "Go back West, to the foyer"},
    "l1_06-05":             {"it": "Vai ad Ovest verso la stanza vuota",                "en": "Go back West, to the empty room"},
    "06pickup":             {"it": "Cerca tra i resti dell'imp",                        "en": "Search the imp's ashes"},
    "06drink":              {"it": "Abbeverati alla fontana",                           "en": "Drink at the fountain"},
    "06attack":             {"it": "Attacca l'imp",                                     "en": "Attack the imp"},
    "l1_14-04":             {"it": "Vai verso l'atrio",                                 "en": "Go towards the foyer"},
    "l1_14-24":             {"it": "Continua a percorrere il corridoio verso Sud",      "en": "Keep following the corridor South"},
    "l1_24-14":             {"it": "Percorri il corridoio verso nord",                  "en": "Follow the corridor in North direction"},
    "l1_25-24":             {"it": "Torna indietro nel corridoio",                      "en": "Go back in the corridor"},
    "25kill":               {"it": "Uccidi la guardia nel sonno",                       "en": "Kill the guard in his sleep"},
    "25dialog":             {"it": "Parla con la guardia",                              "en": "Speak with the guard"},
    "25attack":             {"it": "Attacca la guardia",                                "en": "Attack the guard"},
    "25inspect":            {"it": "Cerca nel cadavere",                                "en": "Inspect the dead body"},
    "34attack":             {"it": "Attacca lo zombie",                                 "en": "Attack the zombie"},
}

callbacks_translations = {
    "l1_st06fight" :        {"it":"\n\n---------------------------------\n\nMentre osservi la fontana con occhi curiosi, un'entità malvagia e ripugnante si innalza in volo.\nDai suoi occhi percepisci una volontà mortale.",
                             "en":"\n\n---------------------------------\n\nAs you observe the fountain with curious eyes, an evil and repulsive entity soars into flight.\nFrom his eyes you perceive a deadly will."},
    "l1_rs06fight" :        {"it":"\n\n---------------------------------\n\nUna massa nera, putrescente e informe giace dov'era un tempo l'imp.",
                             "en":"\n\n---------------------------------\n\nA black, rotting, shapeless mass lies where was once the imp."},
    "l1_25sleep" :          {"it":"\n\n---------------------------------\n\nLa guardia se ne sta a terra, su quello che sembra un letto fatto di paglia, e sembra dormire.",
                             "en":"\n\n---------------------------------\n\nThe guard is on the ground, come on what looks like a bed made \nof straw, and seems to sleep."},
    "l1_25dead-taken" :     {"it":"\n\n---------------------------------\n\nla guardia giace a terra, in una pozza di sangue.",
                             "en":"\n\n---------------------------------\n\nThe guard lays on the ground in a puddle of blood."},
    "l1_25encounter" :      {"it":"\n\n---------------------------------\n\nC'è una vecchia guardia poggiata al tavolo, si gira e ti osserva con occhi spalancati.",
                             "en":"\n\n---------------------------------\n\nThere is an old guard leaning over the table, turns and looks at you with eyes wide open."},
    "l1_25dead-items" :     {"it":"\n\n---------------------------------\n\nla guardia giace a terra, in una pozza di sangue. Sembra che abbia con se degli oggetti.",
                             "en":"\n\n---------------------------------\n\nThe guard is lying on the ground \nin a puddle blood. Looks like he's carrying items."},
    "l1_34fight" :          {"it":"\n\n---------------------------------\n\nAperta la porta un'immondo fetore di putrefazione colpisce i tuoi sensi, e poi incredulo osservi le orbite vuote un cadavere mentre lui, con movimenti rotti, avanza inesorabile verso di te.",
                             "en":"\n\n---------------------------------\n\nUpon opening the door, a foul stench of decay assaults your senses, and then you incredulously observe the empty eye sockets of a corpse as it, with jerky movements, advances inexorably towards you."},
    "l1_34dead" :           {"it":"\n\n---------------------------------\n\nQualsiasi forza muovesse il cadavere sembra ora svanita, giace, con la mandibola dislocata in una smorfia che sembra ringraziarti del dono della pace eterna.",
                             "en":"\n\n---------------------------------\n\nWhatever force moved the corpse now seems to have vanished, it lies with its jaw dislocated in a grimace that seems to thank you for the gift of eternal peace."},
    "l1_03sword" :          {"it":"\n\n---------------------------------\n\nHai recuperato una spada d'acciaio di squisita fattura. (For. +2)",
                             "en":"\n\n---------------------------------\n\nYou have recovered an exquisite \nsteel sword invoice.(Str. +2)"},
    "l1_dooropen" :         {"it":"\n\n---------------------------------\n\nHai aperto la porta.",
                             "en":"\n\n---------------------------------\n\nYou open the door."},
    "l1_nokey" :            {"it":"\n\n---------------------------------\n\nNon hai la chiave.",
                             "en":"\n\n---------------------------------\n\nYou don't have the key."},
    "l1_pickupkey" :        {"it":"\n\n---------------------------------\n\nHai raccolto la chiave.",
                             "en":"\n\n---------------------------------\n\nYou pick up the key."},
    "l1_pickupkeyimp" :     {"it":"\n\n---------------------------------\n\nHai raccolto la chiave dell'imp.",
                             "en":"\n\n---------------------------------\n\nYou pick up the imp's key."},
    "l1_pickupkeydead" :    {"it":"\n\n---------------------------------\n\nHai raccolto la chiave dal cadavere.",
                             "en":"\n\n---------------------------------\n\nYou pick up the key from the dead body."},
    "l1_25gosleep" :        {"it":"\n\n---------------------------------\n\nLa guardia si sdraia a terra, su quello che sembra un letto fatto di paglia, \ne cerca di addormentarsi.",
                             "en":"\n\n---------------------------------\n\nThe guard lies down on the ground, on what it looks like a bed made \nof straw, and trying to fall \nasleep."},
    "l1_r06drink" :         {"it":"\n\n---------------------------------\n\nSenti la forte energia di centinaia di anime che ti permea. (Mana +2)",
                             "en":"\n\n---------------------------------\n\nYou feel the strenght of hundreds souls infused within you. (Mana +2)"},
    "l1_r06drink" :         {"it":"\n\n---------------------------------\n\nSenti la forte energia di centinaia di anime che ti permea. (Mana +2)",
                             "en":"\n\n---------------------------------\n\nYou feel the strenght of hundreds souls infused within you. (Mana +2)"},

    "l1_06combat":{"it":"\n\nL'Imp si avventa con voracità famelica in cerca della tua vita",
                   "en":"\n\nThe Imp rushes with ravenous voracity for your life"},
    "l1_25combat":{"it":"\n\n'QUESTO NON E' UN POSTO PER GIROVAGARE' \n\nil vecchio si alza e agita un bastone verso di te.",
                   "en":"\n\n'THIS IS NO PLACE FOR A WALK' \n\nthe old man stands up and waves a wooden rod at you."},
    "l1_34combat":{"it":"\n\nCon un'improvvisa forza sovrumana il cadavere si avventa su di te",
                   "en":"\n\nWith sudden superhuman strength the corpse pounces on you."},

    "l1_25dialog-1":{"it":"\n\n---------------------------------\n\n'CHI SIETE!?' grida la guardia, con voce ferma.",
                     "en":"\n\n---------------------------------\n\n'WHO ARE YOU!?' shouts the guard, in a firm voice."},
    "l1_25dialog-2":{"it":"\n\n---------------------------------\n\n'Neanche io...' sussurra la vecchia guardia, con voce rassegnata.\n'Che vuoi!?' esclama con follia.",
                     "en":"\n\n---------------------------------\n\n'Me neither...' the old guard \nwhispers, with a resigned voice.\n'What do you want!?' he exclaims \nmadly."},
    "l1_25dialog-3":{"it":"\n\n---------------------------------\n\nLa vecchia guardia scoppia a ridere.\n'Non c'è via d'uscita! Questo posto è sigillato da un'antica magia'.\n'Prendi questa chiave, forse tornerà più utile a te che a me.'\n\n---------------------------------\n\nTi porge la chiave.",
                     "en":"\n\n---------------------------------\n\nThe old guard bursts into \nlaughter. \n'There is no way out! \nThis place is sealed by an ancient magic'.\n'Take this key, perhaps it will be of more use to you than to me.'\n\n---------------------------------\n\nHe hands you the key."},
    "l1_25dialog-4":{"it":"\n\n---------------------------------\n\nLa vecchia guardia ti scruta con occhi di incredula gratitudine.\n\n'Grazie', esala dalla bocca.",
                     "en":"\n\n---------------------------------\n\nThe old guard stares at you with \neyes of disbelief gratitude.\n\n'Thank you', he exhales from his \nmouth."},
}
