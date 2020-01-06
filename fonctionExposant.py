
#-----------------------------------------------------------------------------------------------
#Créer une fonction qui prenant en entrée deux parametres et retournant a exposant b
#-----------------------------------------------------------------------------------------------

nombre
def Exposant(nombre,exposant):
  compteur = 0
  resultat = 1#parce que la multiplication par 0 sera 0
  while compteur <exposant:
    resultat = resultat * nombre
    compteur = compteur +1
  return resultat
​
​
​
​
print("entrez nombre a")
a = int(input())
print("entrez nombre exposant")
b = int(input())
​
Exposant(a,b)
​