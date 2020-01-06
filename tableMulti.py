
#-----------------------------------------------------------------------------------------------
#Exercice: Faire un Programme qui demande un chiffre à l'utilisateur et qui affiche sa table de multiplication
#-----------------------------------------------------------------------------------------------

max = 11
compteur = 1
print("Entrez un nombre")
nombre = int(input())
​
while(compteur<max):
  print(nombre,"x",compteur," est égale à",compteur*nombre)
  compteur = compteur+1