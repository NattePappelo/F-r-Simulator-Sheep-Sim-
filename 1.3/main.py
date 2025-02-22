#Farsimulator by Natte Pappelo
version = "1.3"


import json


#importing the config file
configFile = open("config.txt", "r")
config = configFile.read().splitlines()



#removing comments and empty lines
comments = []

for i in range(len(config)):
    if config[i] == "":
        comments.append(i)
    elif config[i][0] == "#":
        comments.append(i)

comments.reverse()

for i in comments:
    config.pop(i)




#gets the languages from the config file
languageConfigIndex = config.index("Languages:")
languageFiles = []

for i in range(languageConfigIndex + 1, len(config)):
    if config[i] == "end":
        break
    languageFiles.append(config[i])
    




#opens the language files
languages = []
for i in range(len(languageFiles)):
    languages.append(json.load(open(languageFiles[i], encoding="utf-8")))






#from config import languages



#this is the text in the beginning of the game that asks for a number that coresponds to the selected language

if len(languages) == 0:
    print("No languages found")
    exit()

elif len(languages) == 1:
    oneLanguage = True

else:
    oneLanguage = False
    first = True

    for i in languages:
        if first:
            chooseLanguage = i["chooseLanguage"]
        else:
            chooseLanguage = chooseLanguage + " / " + i["chooseLanguage"]
        first = False

    first = True

    for i in languages:
        if first:
            chooseLanguage = chooseLanguage + "\n" + i["language"] + " = " + i["ifAnything"]
        else:
            chooseLanguage = chooseLanguage + " / " + i["language"] + " = " + str(languages.index(i))
        first = False

if not(oneLanguage):
    print(chooseLanguage)




    #this converts the number to the selected language
    langnum = input()

    try:
        langnum = int(langnum)
    except:
        langnum = 0


    if langnum >= len(languages):
        langnum = 0
    elif langnum < 0:
        langnum = 0

else:
    langnum = 0



language = languages[langnum]


def text(frase):
    return language[frase]




#The game
playing = True

while playing:
    print(text("welcome") + version)
    print()
    
    living = True
    
    while living == True:
        print(text("order"))
        ba = input()
        if ba in text("bleats"):
            print(text("compliment"))
            print()
        
        else:
            living = False
            print()
            print(text("over"))
        
        
    
    print()
    print(text("again"))
    if input() in text("yes"):
        pass
    
    else:
        playing = False
    


