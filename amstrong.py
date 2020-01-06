#-----------------------------------------------------------------------------------------------
#Ecrire un programme detectant les nombres de Amstrong compris entre 0 et 999 
#Un chiffre de Amstrong est un chiffre dont par exemple il faut que 142 = la somme des chiffres qu'il compose au cube 1e3 + 4e3 +2e3 
#Solution du prof ==> Pour montrer qu'on peut mettre des boucles dans des boucles Pour savoir
#-----------------------------------------------------------------------------------------------
[ ]
i=0
j=0
k=0
while i<10:
  while j<10:
    while k<10:
      if (i*i*i + j*j*j + k*k*k) == (i*100 + j*10 + k) :
        print(i*100 + j*10 +k)
      k=k+1
    j=j+1
  i=i+1
