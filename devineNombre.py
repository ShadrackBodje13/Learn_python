#-----------------------------------------------------------------------------------------------
#Programme qui fait deviner mon nombre au joueur
#-----------------------------------------------------------------------------------------------


print("Entrez valeur 1")
valeur1 = int(input())
print("Entrez valeur 2")
valeur2 = int(input())
print("Entrez valeur 3")
valeur3 = int(input())

if valeur1 < valeur2 and valeur1 < valeur3 :
  print("La plus petite valeur est")
  print(valeur1)
if valeur2 < valeur1 and valeur2 < valeur3 :
  print("la plus petite valeur est")
  print(valeur2)
else : 
  print("la plus petite valeur est")
  print(valeur3)