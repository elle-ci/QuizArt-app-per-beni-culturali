import json
import sys

def voto(d):
    sum = 0
    tot=0
    for v in d.values():
        tot+=v
    for i, v in enumerate(list(d.values())):
        sum += (i+1)*v
    return round((sum*10)/(4*tot), 2)

def percentuale(d):
    sum = 0
    tot=0
    l = []
    string = ""
    for k, v in d.items():
        if k == "altro": continue
        tot+=v
    for i, k in enumerate(d.keys()):
        if k == "altro": continue
        l.append(((d[k]/tot)*100, k))
        sum += d[k]/tot
    l.sort(key=lambda x: (-x[0], x[1]))
    for perc, s in l:
        if perc == 0: break
        if s == "Sfidare i tuoi amici": s = "Sfidare gli amici"
        string += s+"({}%), ".format(round(perc, 2))
    string = string[:-2]+";"
    return string

sys.stdout = open('Microanalisi questionario.txt', 'a')

with open("results.json") as f:
  data = json.load(f)
for age in data.keys():
    for sex in data[age].keys():
        d = data[age][sex]
        print("{}, {}: {} persone".format(sex, age, d["# intervistati"]))
        if d["# intervistati"] > 0:
            print("- Visitano annualmente beni culturali:")
            print("\t{}".format(percentuale(d["# visite annue"])))
            if d["# visite annue"]["0"] != d["# intervistati"]:
                print("chi li visita lo fa nelle seguenti occasioni:")
                print("\t{}".format(percentuale(d["occasioni visite"])))
                print("e si informa riguardo ai beni culturali tramite:")
                print("\t{}".format(percentuale(d["canali informativi"])))
            print("- Il problema covid ha inficiato sulla frequenza di visita dei beni culturali:")
            print("\t{}".format(percentuale(d["influenza Covid-19"])))
            print("- Ció che li frena nella visita di beni culturali è:")
            print("\t{}".format(percentuale(d["demotivazioni visite"])))
            print("- Scaricano app a tema arte:")
            print("\t{}".format(percentuale(d["scaricato app arte"])))
            print("- Scaricano giochi a quiz:")
            print("\t{}".format(percentuale(d["giocatore di quiz"])))
            if d["giocatore di quiz"]["No"] > 0:
                print("chi non scarica giochi a quiz é perché:")
                print("\t{}".format(percentuale(d["motivazioni NON download app quiz"])))
            print("chi ha risposto si gioca a quiz per:")
            print("\t{}".format(percentuale(d["motivazioni download app quiz"])))
            print("chi ci gioca conosce:")
            print("\t{}".format(percentuale(d["app conosciute"])))
            print("- Parere app quiz tema arte:")
            print("\t{}".format(percentuale(d["parere app quiz tema arte"])))
            l = [
                (voto(d["utilita' quiz"]), "utilita' quiz"),
                (voto(d["bacheca informativa"]), "bacheca informativa"),
                (voto(d["curiosita'"]), "curiosita'"),
                (voto(d["classifica"]), "classifica"),
                (voto(d["vincere buoni"]), "vincere buoni"),
                (voto(d["tema settimanale"]), "tema settimanale")
                ]
            l.sort(key=lambda x: (-x[0], x[1]))
            for t in l:
                if t[1] == "utilita' quiz":
                    print("- Valutano {}/10 l’utilitá dei giochi a quiz;".format(voto(d["utilita' quiz"])))
                elif t[1] == "bacheca informativa":
                    print("- Valutano {}/10 l’utilitá della bacheca informativa;".format(voto(d["bacheca informativa"])))
                elif t[1] == "curiosita'":
                    print("- Valutano {}/10 l’utilitá delle curiositá durante il quiz;".format(voto(d["curiosita'"])))
                elif t[1] == "classifica":
                    print("- Valutano {}/10 l’utilitá della classifica tra amici;".format(voto(d["classifica"])))
                elif t[1] == "vincere buoni":
                    print("- Valutano {}/10 l’utilitá di vincere dei buoni;".format(voto(d["vincere buoni"])))
                elif t[1] == "tema settimanale":
                    print("- Valutano {}/10 l’utilitá dei temi settimanali.".format(voto(d["tema settimanale"])))
        print("")
