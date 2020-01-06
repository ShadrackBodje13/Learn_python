#-------------------------------------------------------------------------------
#Créer une fonction prenant 2 parametres et retournant le plus grand des deux
#-------------------------------------------------------------------------------


def PlusGrand(parametre1, parametre2):
  if parametre1 < parametre2 :
    #print("Le plus garnd des deux nombres est", parametre2)
    return parametre2
  else:
    #print("Le plus grand des deux nombres est", parametre1)
    return parametre2
  
print("Entrez nombre1")
nombre1 = int(input())
print("Entrez nombre2")
nombre2 = int(input())
​
PlusGrand(nombre1, nombre2)