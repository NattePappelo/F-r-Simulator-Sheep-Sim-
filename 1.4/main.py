#Fårsimulator by Natte Pappelo
version = "1.4"


import json


#importing the config file
try:
    configFile = open("config.txt", "r")
except:
    print("ERROR: No config.txt file found")
    input()
    exit()
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
try:
    languageConfigIndex = config.index("Languages:")
except:
    print("ERROR: No languages found in config.txt")
    input()
    exit()
languageFiles = []

for i in range(languageConfigIndex + 1, len(config)):
    if config[i] == "end":
        break
    languageFiles.append(config[i])
    




#opens the language files
languages = []
for i in range(len(languageFiles)):
    try:
        languages.append(json.load(open(languageFiles[i], encoding="utf-8")))
    except:
        print("ERROR: No languagepack named \"" + languageFiles[i] + "\" was found")
        input()
        exit()
    




#this is the text in the beginning of the game that asks for a number that coresponds to the selected language

if len(languages) == 0:
    print("ERROR: No languages found in config.txt")
    input()
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
    try:
        return language[frase]
    except:
        print("ERROR: Found no phrase in the language pack called \"" + frase + "\"")
        input()
        exit()




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
    


