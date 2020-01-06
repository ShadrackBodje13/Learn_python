#-----------------------------------------------------------------------------------------------
#Ecrire un algorithme qui affiche les 20 premiers chiffres pairs(multiple de deux=son modulo = 0)
#-----------------------------------------------------------------------------------------------

nb1 = 0
compteur =0#0 est multiple de 2
while compteur <40: #faire 20 fois
  if compteur%2 == 0:
    print(compteur) 
  compteur = compteur +1
​
#autre solution
#while compteur <20:
#  print(compteur*2)
#compteur = compteur +1
#