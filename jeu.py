import random
j = 0
p = 0
for  i in range (10):
	x = int(input ("Donner un nombre 0 ou 1 ou 2: "))
	y = random.randint (0,2)
	print ("le choix de l'ai: ")
	if x+2 == y or x-2==y:
		p = p+1
	elif y+1 == x or y-1 == x:
		j = j+1
	else:
		j = j
		p = p
	print ("L'ia: ",p)
	print ("Toi: ",j)
print ("Les resultats :")
print ("Joueur: ", j)
print ("L'inteligance artificiel: ", p)
if j < p:
	print ("Tu es nul")
else:
	print ("Bravo!!")
input("")
