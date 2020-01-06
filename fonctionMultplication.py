#-----------------------------------------------------------------------------------------------------
#Ecrire une fonction qui prend un parametre et qui affiche la table de multiplicatioin de ce parametre
#-----------------------------------------------------------------------------------------------------
def Multiplication(nombre):
  max = 11
  compteur = 1

  while(compteur<max):
    print(nombre,"x",compteur," est égale à",compteur*nombre)
    compteur = compteur+1

Multiplication(3)