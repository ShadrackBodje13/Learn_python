#-----------------------------------------------------------------------------------------------
#Ecrire un programme qui fait deviner un chiffre à l'utilisateur Tant que l'utilisateur n'a pas rentré le bon,
#on lui resoumet la reponse si le chiffre qu'il a rentré est plus grand on affiche notre chiffre est plus petit Si le chiiffre qu'il a rentré est plus petit,
# on affiche notre chiffre à deviner est Si le chiffre rentré par l'utilisateur est le bon, on affiche victoire
#-----------------------------------------------------------------------------------------------

monChiffre = int(5)
​
print("Devinez un chiffre")
chiffre = int(input())
while chiffre != monChiffre :
  if(chiffre < monChiffre):
    print("Mon chiffre est plus grand")
  elif(chiffre > monChiffre):
    print("Mon chiffre est plus petit")
  chiffre = int(input())
 #-----------------
if (chiffre == monChiffre):
    print("Victoire")