# BICZO Samuel
# Groupe 4-1

#######################
# importations
#######################
from mots import MOTS
from figures_pendu import FIGURES_PENDU
import random
#######################
# fonctions
#######################
def choisit_mot():
    """
    rien -> chaine de caractère 
    
    Retourne un mot au hasard présent dans la liste de MOTS   
    """
    return MOTS[random.randint(0, len(MOTS) -1)].lower() # Je mets quand même en minuscule car on sait jamais que MOTS contient TOTO par exemple que j'aurai voulu rajouter moi même
def est_dans(caractere, mot):
    """
    chaine de caractère, chaine de caractère -> booléan
    
    Retourne True si le caractère est présent dans le mot et False sinon  
    """
    return caractere in mot
def input_lettre(props):
    """
    chaine de caractère -> chaine de caractère
    
    Demande une saisi d'une chaine de caractère qui contient une unique lettre non présente dans props
    """
    
    while True:
        lettre = input("Proposez une lettre : ").lower()
        
        if len(lettre) == 0 or len(lettre) > 1:
            print("Proposez une seule lettre, s’il vous plaît.")
        elif est_dans(lettre, props):
            print("Vous avez déjà proposé cette lettre.")
        elif ord(lettre) < ord('a') or ord(lettre) > ord('z'):
            print("{} n’est pas une lettre.".format(lettre))
        else:
            return lettre
        
def dessine_pendu(n):
    """
    entier -> rien
    
    Affiche a l'écran le nième élement de FIGURES_PENDU a l'écran
    """
    print(FIGURES_PENDU[n])
    
def affiche_erreurs(erreurs):
    """
    chaine de caractère -> rien
    
    Affiche a l'écran lettres proposer n'étant pas dans le mot piocher au hasard
    """
    
    print("Erreurs :")
    for l in erreurs:
        print("{} ".format(l), end="")
    print("")
    
def affiche_correctes(correctes, mot_secret):
    """
    chaine de caractère, chaine de caractère -> rien
    
    Affiche a l'écran les bonne lettres saisit par l'utilisateur pour composer le mot piocher
    """
    lettre_presentes = []
    
    for l in correctes:
        if est_dans(l, mot_secret):
            lettre_presentes.append(l)
    
    for l in mot_secret:
        if l in lettre_presentes:
            print("{} ".format(l), end="")
        else:
            print("_ ", end="")
    print("")
    
    
    
def gagne(props, mot_secret):
    """
    chaine de caractère, chaine de caractère -> booléan
    
    Retourne True si l'utilisateur a trouver le mot secret (en proposant toutes les lettre contenu dans ce mot) et Faux sinon
    """
    status = []
    
    for l in mot_secret:
        status.append(est_dans(l, props))
        
    for etat in status:
        if etat == False:
            return False
    return True 
    
def main():
    """
        LE JEUX DU PENDU !!!
    """
    
    jouer = True
    
    while jouer:
        print("LE PENDU")
        dessine_pendu(len(FIGURES_PENDU)-1)
        print("NOUVELLE PARTIE...")
        mot_secret = choisit_mot()
        
        compteur = 0
        erreurs = ""
        correctes = ""
        joueur_gagne = False
        
        print("JE TRICHE : " + mot_secret)
        
        while compteur < len(FIGURES_PENDU)-1:
            dessine_pendu(compteur)
            affiche_erreurs(erreurs)
            affiche_correctes(correctes, mot_secret)
            lettre = input_lettre(erreurs + correctes)
            
            if est_dans(lettre, mot_secret):
                correctes += lettre
            else:
                erreurs += lettre
                compteur += 1
                
            joueur_gagne = gagne(correctes, mot_secret)
            
            if joueur_gagne:
                print("Vous avez gagner !")
                compteur = len(FIGURES_PENDU)

                
        if joueur_gagne == False:
            dessine_pendu(compteur)
            print("Vous avez perdu !")
        
        continuer = input("Voulez-vous continuer ? [O/n]").lower()
        
        if continuer == 'n':
            jouer = not jouer
        
            
            
            
    
    