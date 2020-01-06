#-----------------------------------------------------------------------------------------------
#Créer une fonction prenant deux parametres et,propose à l'utilisateur d'afficher soit le plus petit soit le plus grand des deux chiffres 
#-----------------------------------------------------------------------------------------------
[ ]
def Mini(parametre1, parametre2):
  if parametre1 < parametre2 :
    return parametre1
  else:
    return parametre2
    
def Max(parametre1, parametre2):
  if parametre1 < parametre2 :
    return parametre2
  else:
    return parametre1
  
  
def ChoixMinMax(parametre1,parametre2):
  choix = input()
  if choix == "min":
    return Mini(parametre1,parametre2)
  elif choix == "max":
    return Max(parametre1,parametre2)
    
    
n1 = int(input())
n2 = int(input())
m = ChoixMinMax(n1,n2)
print(m)