#on ajoute le module "random" pour pouvoir utiliser la fonction "randint"
import random
#on definit la variable "n" pour plus tard
n="o"
#cette variable sert à compter le nombre d'essais que le joueur a fait
essais=1
#la variable record servira a enregistrer les futurs records
record=100
#tant que la variable "n" est egale a o(oui), le programme continue
while n=="o":
#la fonction randint sert a generer un nombre aleatoire entre 1 et 100
  p=random.randint(0,100)
#cette variable sert de stockage pour la reponse du joueur
  t=101
#tant que la variable "t" definit plus haut ne sera pas egale a "p" alors la boucle tournera
  while int(t)!=p:
#on definit la variable "t" en reponse a la question ci-dessous
    t=input("Donnez un entier entre 0 et 100 inclus : ")
#si "t" est inferieure a "p", il y aura marque "C'est plus !"
    if int(t)<p:
      print("C'est plus")
#A l'inverse, si "t" est superieur a p, alors il y aura marque "C'est moins"
    if int(t)>p:
      print("C'est moins")
#on augmente le nombre d'essais du joueur de 1, à chaque tentative
    essais+=1
#Si "t" est egale a p alors le joueur a gagne et "Bravo !!!!" s'affiche
    if int(t)==p:
#si le nombre d'essais est inferieur a l'ancien record, le nombre d'essais sera stockee dans la variable "record" et deviendra le nouveau record
      if record>essais:
        record=essais
        print("Bravo !!!!")
        print("Vous avez battu l'ancien record.")
      else:
        print("Bravo !")
#permet d'afficher le nombre a trouver et le nombre d'essais effectue
      print("Vous avez réussi à trouver "+str(p)+" en "+str(essais)+" essais.")
#permet d'afficher le record
      print("Le record est de "+str(record)+" essais.")
      essais=1
#on propose au joueur de recommencer. La variable n est utilisee pour stocker "o" pour oui ou "n" pour non
  n=input("Voulez-vous recommencer (o pour oui et n pour non) ? ")
  if n == "o":
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
  else:
    print("Dommage :(")
    print("Au revoir.")
