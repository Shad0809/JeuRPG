from competences import competence_raciale_auto, competence_metier_auto
from competences import competences_optionnelles_race, competences_optionnelles_metier
from personnage import Personnage
from utils import afficher_title, choix_numero

# ------------------ COMPÉTENCES ------------------

def competence():
    # Affiche les compétences des races
    print("------------- Compétences selon les races -------------\n")

    print("Gamer : Le Mode Rage")
    print("Effet : Colère du Déconnecté — Quand le ping est trop haut ou qu'un *bug* survient, le Gamer active son 'Mode Rage' !")
    print("        Il éclate violemment clavier, souris, ou manette sur son adversaire le plus proche, infligeant")
    print("        des dégâts bonus considérables et ayant une chance d'étourdir la cible pour 1 tour.")
    print("        Malheureusement, il doit racheter son équipement après ça.\n")

    print("Repugnant : Le Repoussoir Social")
    print("Effet : Éloignement Forcé — L'odeur du Répugnant est si catastrophique et l'hygiène si absente")
    print("        que même l'ennemi le plus coriace (hormis les Boss) doit immédiatement fuir 2 cases en arrière.\n")

    print("Poids lourds : Impact Sismique")
    print("Effet : Onde de Choc Calorique — Le Poids Lourd provoque une secousse tellurique,")
    print("        déstabilisant les ennemis proches (chance d'étourdir 1 tour).\n")

    # Compétences des métiers
    print("------------- Compétences selon les métiers -------------\n")

    print("Le Bio-Purificateur : Purge Vitale")
    print("Effet : Absorption — Inflige des dégâts légers mais soigne le lanceur d'une petite partie du total.\n")

    print("Le Négociateur : Manipulation de Valeur")
    print("Effet : L'Offre Qu'on Ne Refuse Pas — Oblige un ennemi à rater son prochain jet d'attaque ou à cibler un allié précis.\n")

    print("Le Mastodonte : Protection Totale")
    print("Effet : Bouclier Brut — Confère un bouclier temporaire de 40 PV pendant 2 tours.\n")

    print("-------------------------------------------------------\n")

    # Pause et retour au menu
    input("Appuie sur Entrée pour retourner au menu...")
    return menu()   # Retourne au menu principal

# ------------------ SÉLECTION PERSONNAGE ------------------

def personnage():
    # Menu des races
    print("Choisissez votre race")
    print("1 - Gamer")
    print("2 - Repugnant")
    print("3 - Poids lourds\n")

    choix = input("Choisis la race: ")

    if choix == "1":
        return "Gamer"
    elif choix == "2":
        return "Repugnant"
    elif choix == "3":
        return "Poids lourds"
    else:
        print("Choix invalide, réessaie !\n")
        return personnage()

def metier():
    # Menu des métiers
    print("Maintenant choisissez votre metier")
    print("1 - Le Bio-Purificateur")
    print("2 - Le Négociateur")
    print("3 - Le Mastodonte")

    choix = input("Choisissez le metier : ")

    if choix == "1":
        return "Le Bio-Purificateur"
    elif choix == "2":
        return "Le Négociateur"
    elif choix == "3":
        return "Le Mastodonte"
    else:
        print("Choix invalide, réessaie !\n")
        return metier()

# ------------------ CHOIX DES COMPÉTENCES OPTIONNELLES ------------------

def choisir_competence_optionnelle_race(race):
    afficher_title(f"Compétences optionnelles pour la race : {race}") #Affichage du titre
    options = list(competences_optionnelles_race[race].keys()) #Récupération de la liste des compétences disponibles

    for i, nom in enumerate(options, start=1): #Affichage des compétences avec leurs bonus
        b = competences_optionnelles_race[race][nom]
        print(f"{i} - {nom}  (PV{b['pv']}  ATK{b['attaque']}  VIT{b['vitesse']}  DEF{b['defense']})")

    choix = choix_numero("Choisis 1 compétence (1-4) : ", 4) #Le joueur fait son choix
    return options[choix - 1] #Retourne la compétence choisie

def choisir_competence_optionnelle_metier(metier):
    afficher_title(f"Compétences optionnelles pour le métier : {metier}")
    options = list(competences_optionnelles_metier[metier].keys())
    for i, nom in enumerate(options, start=1):
        b = competences_optionnelles_metier[metier][nom]
        print(f"{i} - {nom}  (PV{b['pv']}  ATK{b['attaque']}  VIT{b['vitesse']}  DEF{b['defense']})")
    choix = choix_numero("Choisis 1 compétence (1-4) : ", 4)
    return options[choix - 1]

# ------------------ MENU PRINCIPAL ------------------

def menu():
    print("---------Menu---------")
    print("1 - Information sur les compétences et les races")
    print("2 - Commencer à jouer\n")

    choix = input("Choisir 1 pour voir les compétences ou 2 pour commencer : ").strip()

    if choix == "1":
        return competence()

    elif choix == "2":
        # Choix race
        race = personnage()
        comp_race_auto = competence_raciale_auto[race]
        # Choix compétence optionnelle raciale
        comp_race_choisie = choisir_competence_optionnelle_race(race)

        # Choix metier
        met = metier()
        comp_metier_auto = competence_metier_auto[met]
        # Choix compétence optionnelle metier
        comp_metier_choisie = choisir_competence_optionnelle_metier(met)

        # Création du personnage et affichage
        perso = Personnage(
            race=race,
            comp_race_auto=comp_race_auto,
            comp_race_choisie=comp_race_choisie,
            metier=met,
            comp_metier_auto=comp_metier_auto,
            comp_metier_choisie=comp_metier_choisie
        )
        perso.afficher_stats()

    else:
        print("Choix invalide !\n")
        return menu()

# ------------------ BOUCLE DE LANCEMENT ------------------

if __name__ == "__main__":
    while True:
        a = input("Menu initial : 1 pour lancer le jeu, 2 pour quitter : ").strip()
        if a == "1":
            menu()
        elif a == "2":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")
