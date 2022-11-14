import random
pasr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "Q", "S", "D","F","G","H","J","K","L","M","W","X","C","V","B","N","1","2","3","4","5","6","7","8","9","0","?",".","/","§","%","&","é","-","_","ç","=","+","*",";",":","!",",","$","^","¤"]
password = ""
for i in range(8,20):
    password = password +random.choices(pasr)[0]
print (password)
input("")
