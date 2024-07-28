import swe
import eng
import fin

lang = 0

print("Choose language / Välj språk / Valitse Kieli")
print("anything = english / 1 = svenska / 2 = suomeksi")
langnum = input()

if langnum == "1":
    lang = "swe"
elif langnum == "2":
    lang = "fin"


def text(frase):
    if lang == "swe":
        return swe.swe[frase]
    elif lang == "fin":
        return fin.fin[frase]
    else:
        return eng.eng[frase]


playing = True

while playing:
    print(text("welcome"))
    print()

    najs = True

    while najs == True:
        print(text("order"))
        ba = input()
        if ba in text("bleats"):
            print(text("compliment"))
            print()
        else:
            najs = False
            print()
            print(text("over"))

    print()
    print(text("again"))
    if input() in text("yes"):
        pass
    else:
        playing = False
