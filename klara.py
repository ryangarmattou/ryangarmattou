#les bibliotheque
import webbrowser
import datetime
now = datetime.datetime.now()
import random

#langue
print ("choose language : EN / FR")
lg = input ("")
#francais
if lg == "FR" or lg =="fr" :
    print ("Salut, je suis klara une assistante virtuelle comment tu t'appelles ?")
    name = input("")
    if (len(name)) >= 4 :
        print ("Enchanté de faire votre connaissance "+ name + ", comment puis-je vous aider ?")
        order = input("")
#les avontages
        if order == ("Que pouvez-vous faire ?") or order == ("que pouvx tu faire") :
            print ("- recherche sur google")
            print ("- recherche sur spotify")
            print ("- recherche sur netflix")
            print ("- recherche sur youtube")
            print ("- deviner l'âge")
            print ("- vous donner le temps")
            print ("- vous donner la date")
            print ("- crédit")
            print ("alors, de quoi avez-vous besoin ?")
            order = input("")
#question bizar
            #question de jeu
            if order == ("qui est né le premier de la poule ou de l'œuf"):
                print ("pour moi, le poulet né le premier")
                why = input 
                if why == ("Pourquoi") or why == ("prq") :
                    print ("je ne sais pas, c'est mon opinion")
                    input("")
            #reclamation d'amoure
            elif order == ("est ce que tu m'aime") or order == ("est-ce que tu m'aime"):
                print ("oui, bien sure je t'aime")
                input("")
#random
        elif order == ("choisir un nombre"):
            n = random.randint (0,9)
            print (n)
            input ("")
#age
        elif order == ("devine mon âge") or order == ("devine mon age"):
            print ("Quand es-tu né?")
            yb = int(input (""))
            year = int(now.strftime("%Y"))
            print (year-yb)
            input ("")
            order = input("")
#temps
        elif order == ("Quelle heure est-il") or order == ("donne moi le temps"):
            time = now.strftime ("%H:%M")
            print (time)
            input("")
            order = input("")
#date
        elif order == ("quelle est la date d'aujourd'hui"):
            date = now.strftime ("%d-%m-%Y")
            print (date)
            input("")
            order = input("")
#recherche
        #google
        elif order.find("cherche")!= -1 and order.find("google")!=-1 :
            s = order.index(" ")
            u = order.find("sur")
            sr = order[s:u]
            webbrowser.open('https://www.google.com/search?q='+sr)
        elif order.find("cherche sur google")!=-1:
            sr = order[18:]
            webbrowser.open('https://www.google.com/search?q='+sr)
        #youtube
        elif order.find("cherche")!= -1 and order.find("youtube")!=-1 :
            s = order.index(" ")
            u = order.find("sur")
            sr = order[s:u]
            webbrowser.open('https://www.youtube.com/results?search_query='+ sr)
        elif order.find("cherche sur youtube")!=-1:
            sr = order[19:]
            webbrowser.open('https://www.google.com/search?q='+sr)
        #netflix
        elif order.find("cherche")!= -1 and order.find("netflix")!=-1 :
            s = order.index(" ")
            u = order.find("sur")
            sr = order[s:u]
            webbrowser.open('https://www.netflix.com/search?q='+ sr)
        elif order.find("cherche sur netflix")!=-1:
            sr = order[19:]
            webbrowser.open('https://www.google.com/search?q='+sr)
        #spotify
        elif order.find("cherche")!= -1 and order.find("spotify")!=-1 :
            s = order.index(" ")
            u = order.find("sur")
            sr = order[s:u]
            webbrowser.open ('https://open.spotify.com/search/'+ sr)
        elif order.find("cherche sur spotify")!=-1:
            sr = order[19:]
            webbrowser.open('https://www.google.com/search?q='+sr)
        #credit
        elif order == ("le crédit") or order==("qui est le realisateur de klara ?"):
            print("klara réalisé par Ryan Garmattou")
            input("")
        else:
            print ("désolé :/, je ne suis pas développé pour faire cela svp envoyez un message à @imryan.g sur instagram dites lui vos commentaires, merci :)")
            input ("")
    else :
        print ("erreur!")
        input ("")
#englais
elif lg == "EN" or lg == "en":
    print ("Hi, I'm klara a virtual assistant what's your name?")
    name = input("")
    if (len(name)) >= 4 :
        print ("Nice to meet you "+ name + ", how can I help you ?")
        order = input("")
#les avontages
        if order == ("What can you do ?") :
            print ("- search on google")
            print ("- search on spotify")
            print ("- search on netflix")
            print ("- search on youtube")
            print ("- guess the age")
            print ("- give you time")
            print ("- give you the date")
            print ("- credit")
            print ("so what do you need ?")
            order = input("")
#question bizar
#question de jeu
        elif order == ("who was born first from the chicken or the egg"):
            print ("for me, the chicken born first")
            why = input 
            if why == ("why") or why == ("y"):
                print ("I don't know, it's my opinion")
                input("")
#reclamation d'amoure
        elif order == ("i love you") or order==("i love u")or order==("i <3 u"):
            print ("i love you too honey")
            input("")
#random
        elif order.find("choose a number")!=-1:
            if order.find("between")!=-1:
                a = order.find("and")
                w = order[:a]
                pirnt (w)
                input("")
            else:
                n = random.randint (0,9)
                print (n)
                input ("")
#age
        elif order == ("guess my age"):
            print ("When were you born?")
            yb = int(input (""))
            year = int(now.strftime("%Y"))
            print (year-yb)
            input ("")
            order = input("")
#temps
        elif order == ("What time is it") or order==("give me time"):
            time = now.strftime ("%H:%M")
            print (time)
            input("")
            order = input("")
#date
        elif order == ("what is today's date") or order==("what is the date of today"):
            date = now.strftime ("%d-%m-%Y")
            print (date)
            input("")
            order = input("")
#recherche
        #google
        elif order.find("search")!= -1 and order.find("google")!=-1 :
            s = order.index(" ")
            u = order.find("on")
            sr = order[s:u]
            webbrowser.open('https://www.google.com/search?q='+sr)
        elif order.find("search on google")!=-1:
            sr = order[16:]
            webbrowser.open('https://www.google.com/search?q='+sr)
        #youtube
        elif order.find("search")!= -1 and order.find("youtube")!=-1 :
            s = order.index(" ")
            u = order.find("on")
            sr = order[s:u]
            webbrowser.open('https://www.youtube.com/results?search_query='+ sr)
        elif order.find("search on youtube")!=-1:
            sr = order[17:]
            webbrowser.open('https://www.google.com/search?q='+sr)
        #netflix
        elif order.find("search")!= -1 and order.find("netflix")!=-1 :
            s = order.index(" ")
            u = order.find("on")
            sr = order[s:u]
            webbrowser.open('https://www.netflix.com/search?q='+ sr)
        elif order.find("search on netflix")!=-1:
            sr = order[17:]
            webbrowser.open('https://www.google.com/search?q='+sr)
        #spotify
        elif order.find("search")!= -1 and order.find("spotify")!=-1 :
            s = order.index(" ")
            u = order.find("on")
            sr = order[s:u]
            webbrowser.open ('https://open.spotify.com/search/'+ sr)
        elif order.find("search on spotify")!=-1:
            sr = order[17:]
            webbrowser.open('https://www.google.com/search?q='+sr)
        #credit
        elif order == ("credit") or order==("who made klara ?"):
            print("klara directed by Ryan Garmattou")
            input("")
        #bientot
        else:
            print ("sorry :/, I'm not developed to do this please send a message to @imryan.g on instagram tell him your comments, thank you :)")
            input ("")
    else :
        print ("error!")
        input ("")
else:
    print ("klara dont support this language this language")
    input("")
