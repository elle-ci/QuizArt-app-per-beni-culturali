import pandas as pd
import copy
import json
import codecs

question = {
    0   : "Informazioni cronologiche",
    1   : "Genere",
    2   : "Quanti anni hai?",
    3   : "Quanti beni culturali visiti mediamente all'anno?",
    4   : "In quali occasioni visiti beni culturali?",
    5   : "Hai mai scaricato e giocato a giochi a quiz su smartphone?",
    6   : "Come vieni a conoscenza di eventi riguardanti i beni culturali? Di solito come trovi le mostre da visitare?",
    7   : "Il Covid-19 ha inficiato sulla frequenza di visita ai beni culturali?",
    8   : "Cos’è che ti frena di più nell’andare a visitare beni culturali?",
    9   : "Cosa ti ha spinto a scaricare giochi a quiz?",
    10  : "Quanto reputi utile l'uso di giochi a quiz per imparare cose nuove?",
    11  : "Hai mai scaricato un'applicazione che ha come tema l'arte? (app su un museo, informative, etc.)",
    12  : "Una bacheca informativa dedicata ai beni culturali nella tua zona",
    13  : "Curiosità sui temi dei quiz",
    14  : "Classifica per confrontare i propri risultati con quelli degli amici",
    15  : "Quiz con possibilità di vincere buoni per visitare beni culturali",
    16  : "Ogni settimana viene scelto un tema diverso",
    17  : "Perché non hai mai scaricato giochi a quiz?",
    18  : "Cosa ne pensi di un’applicazione a quiz che incoraggia l’utente ad interessarsi ai beni culturali?",
    19  : "Ulteriori consigli o riflessioni che non hai potuto esprimere nelle precedenti domande:",
    20  : "Quali tra queste applicazioni conosci o hai scaricato?"
}

l = []

d3 = {
    "# intervistati" : 0,
    "# visite annue" : {
        "0" : 0,
        "1-2" : 0,
        "3-5" : 0,
        "piú di 5" : 0
    },
    "occasioni visite" : {
        "viaggio" : 0,
        "weekend" : 0,
        "festivita'" : 0,
        "ferie" : 0,
        "altro" : copy.deepcopy(l)
    },
    "canali informativi" : {
        "publicita'" : 0,
        "internet" : 0,
        "social network" : 0,
        "passaparola" : 0,
        "altro" : copy.deepcopy(l)
    },
    "influenza Covid-19" : {
        "Per nulla" : 0,
        "Poco" : 0,
        "Abbastanza" : 0,
        "Molto" : 0
    },
    "demotivazioni visite" : {
        "distanza" : 0,
        "prezzo" : 0,
        "disinteresse" : 0,
        "tempo" : 0,
        "compagnia" : 0,
        "niente" : 0,
        "altro" : copy.deepcopy(l)
    },
    "scaricato app arte" : {
        "Si" : 0,
        "No" : 0
    },
    "giocatore di quiz" : {
        "Sì" : 0,
        "No" : 0
    },
    "motivazioni download app quiz" : {
        "Cultura personale" : 0,
        "Spirito di competizione": 0,
        "Sfidare i tuoi amici" : 0,
        "Vincere premi" : 0,
        "Passatempo" : 0,
        "altro" : copy.deepcopy(l)
    },
    "utilita' quiz" : {
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0
    },
    "app conosciute" : {
        "Quiz duello" : 0,
        "Trivia Crack" : 0,
        "Live Quiz" : 0,
        "altro" : copy.deepcopy(l)
    },
    "motivazioni NON download app quiz" : {
        "mai avuto occasione" : 0,
        "disinteresse" : 0,
        "assenza premi" : 0,
        "incapacita'" : 0,
        "altro" : copy.deepcopy(l)
    },
    "parere app quiz tema arte" : {
        "use & talk" : 0,
        "NOTuse & talk" : 0,
        "NOTuse & NOTtalk" : 0,
        "altro" : copy.deepcopy(l)
    },
    "bacheca informativa" : {
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0
    },
    "curiosita'" : {
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0
    },
    "classifica" : {
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0
    },
    "vincere buoni" : {
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0
    },
    "tema settimanale" : {
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0
    },
    "consigli" : copy.deepcopy(l)
}

d2 = {
    "Maschio" : copy.deepcopy(d3),
    "Femmina" : copy.deepcopy(d3),
    "Altro" : copy.deepcopy(d3),
    "Generale" : copy.deepcopy(d3),
}

d = {
    "Meno di 18" : copy.deepcopy(d2),
    "18-25" : copy.deepcopy(d2),
    "26-35" : copy.deepcopy(d2),
    "36-45" : copy.deepcopy(d2),
    "46-55" : copy.deepcopy(d2),
    "Oltre 55" : copy.deepcopy(d2),
    "Generale" : copy.deepcopy(d2)
}

s = set()
table = pd.read_excel("table.xlsx")
for index, row in table.iterrows():

    d[row[2]][row[1]]["# intervistati"] += 1
    d[row[2]]["Generale"]["# intervistati"] += 1
    d["Generale"][row[1]]["# intervistati"] += 1
    d["Generale"]["Generale"]["# intervistati"] += 1

    d[row[2]][row[1]]["# visite annue"][str(row[3])] += 1
    d[row[2]]["Generale"]["# visite annue"][str(row[3])] += 1
    d["Generale"][row[1]]["# visite annue"][str(row[3])] += 1
    d["Generale"]["Generale"]["# visite annue"][str(row[3])] += 1

    if not pd.isna(row[4]):
        for i in row[4].split(","):
            i = i.strip()
            key = None
            if(i == "Durante un viaggio"):
                key = "viaggio"
            elif(i == "Durante il weekend"):
                key = "weekend"
            elif(i == "Durante le festività" or i == "Durante le festivitá"):
                key = "festivita'"
            elif(i == "Durante le ferie"):
                key = "ferie"
            if key != None:
                d[row[2]][row[1]]["occasioni visite"][key] += 1
                d[row[2]]["Generale"]["occasioni visite"][key] += 1
                d["Generale"][row[1]]["occasioni visite"][key] += 1
                d["Generale"]["Generale"]["occasioni visite"][key] += 1
            else:
                d[row[2]][row[1]]["occasioni visite"]["altro"].append(i)
                d[row[2]]["Generale"]["occasioni visite"]["altro"].append(i)
                d["Generale"][row[1]]["occasioni visite"]["altro"].append(i)
                d["Generale"]["Generale"]["occasioni visite"]["altro"].append(i)

    if not pd.isna(row[6]):
        for i in row[6].split(","):
            i = i.strip()
            key = None
            if(i == "televisione" or i == "riviste..)" or i == "conoscenti...)"):
                continue
            if(i == "Pubblicità (Cartelloni"):
                key = "publicita'"
            elif(i == "Siti internet"):
                key = "internet"
            elif(i == "Social Network"):
                key = "social network"
            elif(i == "Passaparola (Amici"):
                key = "passaparola"
            if key != None:
                d[row[2]][row[1]]["canali informativi"][key] += 1
                d[row[2]]["Generale"]["canali informativi"][key] += 1
                d["Generale"][row[1]]["canali informativi"][key] += 1
                d["Generale"]["Generale"]["canali informativi"][key] += 1
            else:
                d[row[2]][row[1]]["canali informativi"]["altro"].append(i)
                d[row[2]]["Generale"]["canali informativi"]["altro"].append(i)
                d["Generale"][row[1]]["canali informativi"]["altro"].append(i)
                d["Generale"]["Generale"]["canali informativi"]["altro"].append(i)

    d[row[2]][row[1]]["influenza Covid-19"][str(row[7])] += 1
    d[row[2]]["Generale"]["influenza Covid-19"][str(row[7])] += 1
    d["Generale"][row[1]]["influenza Covid-19"][str(row[7])] += 1
    d["Generale"]["Generale"]["influenza Covid-19"][str(row[7])] += 1

    if not pd.isna(row[8]):
        for i in row[8].split(","):
            i = i.strip()
            key = None
            if(i == "Distanza"):
                key = "distanza"
            elif(i == "Prezzo"):
                key = "prezzo"
            elif(i == "Disinteresse"):
                key = "disinteresse"
            elif(i == "Tempo"):
                key = "tempo"
            elif(i == "Compagnia"):
                key = "compagnia"
            elif(i == "Niente"):
                key = "niente"
            if key != None:
                d[row[2]][row[1]]["demotivazioni visite"][key] += 1
                d[row[2]]["Generale"]["demotivazioni visite"][key] += 1
                d["Generale"][row[1]]["demotivazioni visite"][key] += 1
                d["Generale"]["Generale"]["demotivazioni visite"][key] += 1
            else:
                d[row[2]][row[1]]["demotivazioni visite"]["altro"].append(i)
                d[row[2]]["Generale"]["demotivazioni visite"]["altro"].append(i)
                d["Generale"][row[1]]["demotivazioni visite"]["altro"].append(i)
                d["Generale"]["Generale"]["demotivazioni visite"]["altro"].append(i)

    d[row[2]][row[1]]["scaricato app arte"][str(row[11])] += 1
    d[row[2]]["Generale"]["scaricato app arte"][str(row[11])] += 1
    d["Generale"][row[1]]["scaricato app arte"][str(row[11])] += 1
    d["Generale"]["Generale"]["scaricato app arte"][str(row[11])] += 1

    d[row[2]][row[1]]["giocatore di quiz"][str(row[5])] += 1
    d[row[2]]["Generale"]["giocatore di quiz"][str(row[5])] += 1
    d["Generale"][row[1]]["giocatore di quiz"][str(row[5])] += 1
    d["Generale"]["Generale"]["giocatore di quiz"][str(row[5])] += 1

    if not pd.isna(row[9]):
        for i in row[9].split(","):
            i = i.strip()
            key = None
            if(i == "Cultura personale"):
                key = "Cultura personale"
            elif(i == "Spirito di competizione"):
                key = "Spirito di competizione"
            elif(i == "Sfidare i tuoi amici"):
                key = "Sfidare i tuoi amici"
            elif(i == "Vincere premi"):
                key = "Vincere premi"
            elif(i == "Passatempo"):
                key = "Passatempo"
            if key != None:
                d[row[2]][row[1]]["motivazioni download app quiz"][key] += 1
                d[row[2]]["Generale"]["motivazioni download app quiz"][key] += 1
                d["Generale"][row[1]]["motivazioni download app quiz"][key] += 1
                d["Generale"]["Generale"]["motivazioni download app quiz"][key] += 1
            else:
                d[row[2]][row[1]]["motivazioni download app quiz"]["altro"].append(i)
                d[row[2]]["Generale"]["motivazioni download app quiz"]["altro"].append(i)
                d["Generale"][row[1]]["motivazioni download app quiz"]["altro"].append(i)
                d["Generale"]["Generale"]["motivazioni download app quiz"]["altro"].append(i)

    if not pd.isna(row[10]):
        d[row[2]][row[1]]["utilita' quiz"][str(int(row[10]))] += 1
        d[row[2]]["Generale"]["utilita' quiz"][str(int(row[10]))] += 1
        d["Generale"][row[1]]["utilita' quiz"][str(int(row[10]))] += 1
        d["Generale"]["Generale"]["utilita' quiz"][str(int(row[10]))] += 1

    if not pd.isna(row[20]):
        for i in row[20].split(","):
            i = i.strip()
            key = None
            if(i == "Quiz duello"):
                key = "Quiz duello"
            elif(i == "Trivia Crack"):
                key = "Trivia Crack"
            elif(i == "Live Quiz"):
                key = "Live Quiz"
            if key != None:
                d[row[2]][row[1]]["app conosciute"][key] += 1
                d[row[2]]["Generale"]["app conosciute"][key] += 1
                d["Generale"][row[1]]["app conosciute"][key] += 1
                d["Generale"]["Generale"]["app conosciute"][key] += 1
            else:
                d[row[2]][row[1]]["app conosciute"]["altro"].append(i)
                d[row[2]]["Generale"]["app conosciute"]["altro"].append(i)
                d["Generale"][row[1]]["app conosciute"]["altro"].append(i)
                d["Generale"]["Generale"]["app conosciute"]["altro"].append(i)

    if not pd.isna(row[17]):
        for i in row[17].split(","):
            i = i.strip()
            key = None
            if(i == "Non ne ho mai avuto l'occasione"):
                key = "mai avuto occasione"
            elif(i == "Non ho un particolare interesse per i giochi a quiz"):
                key = "disinteresse"
            elif(i == "I giochi a quiz non offrono dei premi interessanti"):
                key = "assenza premi"
            elif(i == "Non sono capace nei giochi a quiz"):
                key = "incapacita'"
            if key != None:
                d[row[2]][row[1]]["motivazioni NON download app quiz"][key] += 1
                d[row[2]]["Generale"]["motivazioni NON download app quiz"][key] += 1
                d["Generale"][row[1]]["motivazioni NON download app quiz"][key] += 1
                d["Generale"]["Generale"]["motivazioni NON download app quiz"][key] += 1
            else:
                d[row[2]][row[1]]["motivazioni NON download app quiz"]["altro"].append(i)
                d[row[2]]["Generale"]["motivazioni NON download app quiz"]["altro"].append(i)
                d["Generale"][row[1]]["motivazioni NON download app quiz"]["altro"].append(i)
                d["Generale"]["Generale"]["motivazioni NON download app quiz"]["altro"].append(i)

    if not pd.isna(row[18]):
        i = row[18]
        key = None
        if(i == "La scaricherei, e la consiglierei"):
            key = "use & talk"
        elif(i == "Non la scaricherei, ma la consiglierei"):
            key = "NOTuse & talk"
        elif(i == "Non la scaricherei, e non la consiglierei"):
            key = "NOTuse & NOTtalk"
        if key != None:
            d[row[2]][row[1]]["parere app quiz tema arte"][key] += 1
            d[row[2]]["Generale"]["parere app quiz tema arte"][key] += 1
            d["Generale"][row[1]]["parere app quiz tema arte"][key] += 1
            d["Generale"]["Generale"]["parere app quiz tema arte"][key] += 1
        else:
            d[row[2]][row[1]]["parere app quiz tema arte"]["altro"].append(i)
            d[row[2]]["Generale"]["parere app quiz tema arte"]["altro"].append(i)
            d["Generale"][row[1]]["parere app quiz tema arte"]["altro"].append(i)
            d["Generale"]["Generale"]["parere app quiz tema arte"]["altro"].append(i)

    d[row[2]][row[1]]["bacheca informativa"][str(row[12])] += 1
    d[row[2]]["Generale"]["bacheca informativa"][str(row[12])] += 1
    d["Generale"][row[1]]["bacheca informativa"][str(row[12])] += 1
    d["Generale"]["Generale"]["bacheca informativa"][str(row[12])] += 1

    d[row[2]][row[1]]["curiosita'"][str(row[13])] += 1
    d[row[2]]["Generale"]["curiosita'"][str(row[13])] += 1
    d["Generale"][row[1]]["curiosita'"][str(row[13])] += 1
    d["Generale"]["Generale"]["curiosita'"][str(row[13])] += 1

    d[row[2]][row[1]]["classifica"][str(row[14])] += 1
    d[row[2]]["Generale"]["classifica"][str(row[14])] += 1
    d["Generale"][row[1]]["classifica"][str(row[14])] += 1
    d["Generale"]["Generale"]["classifica"][str(row[14])] += 1

    d[row[2]][row[1]]["vincere buoni"][str(row[15])] += 1
    d[row[2]]["Generale"]["vincere buoni"][str(row[15])] += 1
    d["Generale"][row[1]]["vincere buoni"][str(row[15])] += 1
    d["Generale"]["Generale"]["vincere buoni"][str(row[15])] += 1

    d[row[2]][row[1]]["tema settimanale"][str(row[16])] += 1
    d[row[2]]["Generale"]["tema settimanale"][str(row[16])] += 1
    d["Generale"][row[1]]["tema settimanale"][str(row[16])] += 1
    d["Generale"]["Generale"]["tema settimanale"][str(row[16])] += 1

    if not pd.isna(row[19]):
        d[row[2]][row[1]]["consigli"].append(str(row[19]))
        d[row[2]]["Generale"]["consigli"].append(str(row[19]))
        d["Generale"][row[1]]["consigli"].append(str(row[19]))
        d["Generale"]["Generale"]["consigli"].append(str(row[19]))

jsonobj = json.dumps(d, ensure_ascii=False, indent = 4)
with open("results.json", "w", encoding = "utf-8") as jsonfile:
    jsonfile.write(jsonobj)
