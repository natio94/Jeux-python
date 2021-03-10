# from ti_system import *
erreur = 0
mot = ""
motsConnu = []
lettresDonnees = []

def afficheNouvelleLettre(lettreAAficher):
    i=0
    for lettre in mot:
        if(lettre==lettreAAficher):
            motsConnu[i]=lettreAAficher
        i+=1

while True:
    while True:
        print("Choisissez un mot que votre adversaire doit deviner . ")
        mot=input("")
        print("Le mot que vous avez choisi est "+mot+". Voulez vous le changer ? (n ou 2 pour non toutes les autres touches pour oui")
        rep=input("")
        if rep=="2"or rep=="n":
            break
    # disp_clr()
    nbLettre=len(mot)
    motsConnu = ['_']*nbLettre

    while erreur<11:
        print("Choisissez une lettre.")
        lettre=input("")
        if lettre in lettresDonnees:
            print("Vous avez deja donné cette lettre.")
        else:
            afficheNouvelleLettre(lettre)
            if lettre in mot:
                print("Cette lettre est dans le mot")
                s=""
                print("Le mot actuel est : "+s.join(motsConnu))
            else:
                erreur+=1
                print("La lettre n'est pas dans le mot. Il vous reste "+str(11-erreur)+" chance.")
        lettresDonnees.append(lettre)
        if erreur==11:
            print("Vous avez perdu.")
        if '_' not in motsConnu:
            print("Bravo !!! Vous avez gagné")
            break
    print("Voulez-vous recommencer ? (n ou 2 pour non toutes les autres touches pour oui)")
    rep=input("")
    if rep=="2"or rep=="n":
        break
