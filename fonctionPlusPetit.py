
#-----------------------------------------------------------------------------------------------
#Créer une fonction prenant 2 parametres et retournant le plus petit des deux
#-----------------------------------------------------------------------------------------------
[ ]
def PlusPetit(parametre1, parametre2):
  if parametre1 < parametre2 :
    print("Le plus petit des deux nombres est", parametre1)
  else:
    print("Le plus petit des deux nombres est", parametre2)
  
print("Entrez nombre1")
nombre1 = int(input())
print("Entrez nombre2")
nombre2 = int(input())
​
PlusPetit(nombre1, nombre2)