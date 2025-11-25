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


# ------------------ DONNÉES DES COMPÉTENCES OPTIONNELLES (bonus stats) ------------------

competences_optionnelles_race = {
    "Gamer": {
        "Le Speedrun Tactique": {"pv": 0, "attaque": 0, "vitesse": 4, "defense": 0},
        "Capture d'Écran": {"pv": 0, "attaque": 5, "vitesse": 0, "defense": 0},
        "La Lecture du Boss": {"pv": 0, "attaque": 6, "vitesse": 0, "defense": 0},
        "Le Taunt Vociférant": {"pv": 0, "attaque": 3, "vitesse": 0, "defense": 2},
    },
    "Repugnant": {
        "Le Repas Miasmatique": {"pv": 20, "attaque": 0, "vitesse": -1, "defense": 0},
        "Le Voile de Mouches": {"pv": 0, "attaque": 0, "vitesse": 0, "defense": 8},
        "La Piste Visqueuse": {"pv": 0, "attaque": 0, "vitesse": 0, "defense": 3},
        "L'Odeur de la Crainte": {"pv": 0, "attaque": 5, "vitesse": 0, "defense": 0},
    },
    "Poids lourds": {
        "Le Dépôt de Graisse": {"pv": 60, "attaque": 0, "vitesse": -2, "defense": 15},
        "L'Écrasement Calorique": {"pv": 20, "attaque": 10, "vitesse": -2, "defense": 0},
        "La Réserve de Snacks": {"pv": 80, "attaque": 3, "vitesse": -3, "defense": 5},
        "La Persistance Grasse": {"pv": 40, "attaque": 0, "vitesse": -1, "defense": 10},
    }

}

competences_optionnelles_metier = {
    "Le Bio-Purificateur": {
        "Le Nuage Désinfectant": {"pv": 10, "attaque": 0, "vitesse": 0, "defense": 2},
        "Le Sceau de Quarantaine": {"pv": 0, "attaque": 0, "vitesse": 0, "defense": 4},
        "La Bombe Fécale": {"pv": 0, "attaque": 6, "vitesse": 0, "defense": 0},
        "Le Laboratoire Portable": {"pv": 15, "attaque": 3, "vitesse": 0, "defense": 0},
    },
    "Le Négociateur": {
        "La Corruption Express": {"pv": 0, "attaque": 6, "vitesse": 0, "defense": 0},
        "Le Bon Deal": {"pv": 10, "attaque": 0, "vitesse": 0, "defense": 0},
        "Le Contrat Piégé": {"pv": 0, "attaque": 4, "vitesse": 0, "defense": 0},
        "L'Évasion Fiscale": {"pv": 0, "attaque": 0, "vitesse": 4, "defense": 0},
    },
    "Le Mastodonte": {
        "Le Blocage Total": {"pv": 0, "attaque": 0, "vitesse": -1, "defense": 20},
        "L'Élan Brutal": {"pv": 0, "attaque": 8, "vitesse": -1, "defense": 0},
        "Le Coup d'Estomac": {"pv": 0, "attaque": 6, "vitesse": 0, "defense": 0},
        "Le Cri de Guerre": {"pv": 0, "attaque": 2, "vitesse": 0, "defense": 10},
    }
}

# Compétences raciales / métiers automatiques (affichage seulement)
competence_raciale_auto = {
    "Gamer": "Le Mode Rage",
    "Repugnant": "Le Repoussoir Social",
    "Poids lourds": "Impact Sismique"
}

competence_metier_auto = {
    "Le Bio-Purificateur": "Purge Vitale",
    "Le Négociateur": "Manipulation de Valeur",
    "Le Mastodonte": "Protection Totale"
}


# ------------------ AIDES UTILITAIRES ------------------

def afficher_title(txt):
    print("\n" + "-" * 12 + " " + txt + " " + "-" * 12 + "\n")


def choix_numero(prompt, n):
    """Retourne un int valide entre 1 et n."""
    while True:
        rep = input(prompt).strip()
        if rep.isdigit():
            val = int(rep)
            if 1 <= val <= n:
                return val
        print(f"Entrée invalide. Tape un nombre entre 1 et {n}.")


# ------------------ CHOIX DES COMPÉTENCES OPTIONNELLES ------------------

def choisir_competence_optionnelle_race(race):
    afficher_title(f"Compétences optionnelles pour la race : {race}") #Affichage du titre
    options = list(competences_optionnelles_race[race].keys()) #Récupération de la liste des compétences disponibles

    for i, nom in enumerate(options, start=1): #Affichage des compétences avec leurs bonus
        b = competences_optionnelles_race[race][nom]
        print(f"{i} - {nom}  (PV{b['pv']}  ATK{b['attaque']}  VIT{b['vitesse']}  DEF{b['defense']})")

    choix = choix_numero("Choisis 1 compétence (1-4) : ", 4) #Le joueur fait son choix

    return options[choix - 1] #Retourne la compétence choisie

#Idem Fonction chosir la competence

def choisir_competence_optionnelle_metier(metier):
    afficher_title(f"Compétences optionnelles pour le métier : {metier}")
    options = list(competences_optionnelles_metier[metier].keys())
    for i, nom in enumerate(options, start=1):
        b = competences_optionnelles_metier[metier][nom]
        print(f"{i} - {nom}  (PV{b['pv']}  ATK{b['attaque']}  VIT{b['vitesse']}  DEF{b['defense']})")
    choix = choix_numero("Choisis 1 compétence (1-4) : ", 4)
    return options[choix - 1]


# ------------------ CLASSE PERSONNAGE ------------------

class Personnage:
    def __init__(self, race, comp_race_auto, comp_race_choisie,
                 metier, comp_metier_auto, comp_metier_choisie):

        #enregistre la race et le métier dans l’objet
        self.race = race
        self.metier = metier

        # compétences (noms)
        #On stocke les noms des compétences du personnage
        self.comp_race_auto = comp_race_auto
        self.comp_race_choisie = comp_race_choisie
        self.comp_metier_auto = comp_metier_auto
        self.comp_metier_choisie = comp_metier_choisie

        # stats de base
        #Stats de base communes à tous les personnages
        self.pv = 100
        self.attaque = 10
        self.vitesse = 10
        self.defense = 0

        # Appliquer bonus des compétences optionnelles  et on applique automatiquement les bonus
        self.appliquer_bonus_optionnels()

    #Modifie les stats du personnage en fonction des compétences choisies
    def appliquer_bonus_optionnels(self): #
        # race optionnelle / on récupère l’objet bonus
        if self.comp_race_choisie:
            bonus = competences_optionnelles_race[self.race][self.comp_race_choisie]
            self.pv += bonus.get("pv", 0) #Get c'est pour rajouter sinon c'est 0 en fonction de du bonus choisi
            self.attaque += bonus.get("attaque", 0)#Idem que GET PV
            self.vitesse += bonus.get("vitesse", 0)#Idem que GET PV
            self.defense += bonus.get("defense", 0)#Idem que GET PV

        # Metier optionnel / Idem que comp_race_choisie
        if self.comp_metier_choisie:
            bonus = competences_optionnelles_metier[self.metier][self.comp_metier_choisie]
            self.pv += bonus.get("pv", 0)
            self.attaque += bonus.get("attaque", 0)
            self.vitesse += bonus.get("vitesse", 0)
            self.defense += bonus.get("defense", 0)

    def afficher_stats(self):
        afficher_title("FICHE PERSONNAGE") # On rappel pour le titre stylisé

        #Affichage des informations du personnage
        print(f"Race : {self.race}")
        print(f"Compétence raciale : {self.comp_race_auto}")
        print(f"Compétence raciale choisie : {self.comp_race_choisie}\n")
        print(f"Métier : {self.metier}")
        print(f"Compétence de métier : {self.comp_metier_auto}")
        print(f"Compétence métier choisie : {self.comp_metier_choisie}\n")

        #Affichage des stats finales
        print("----- STATS FINALES -----")
        print(f"PV : {self.pv}")
        print(f"Attaque : {self.attaque}")
        print(f"Vitesse : {self.vitesse}")
        print(f"Défense : {self.defense}")

        #Affichage des bonus appliqués
        print("\n---- BONUS APPLIQUÉS ----")
        if self.comp_race_choisie:
            print(f"Bonus (race) : {competences_optionnelles_race[self.race][self.comp_race_choisie]}")
        if self.comp_metier_choisie:
            print(f"Bonus (metier) : {competences_optionnelles_metier[self.metier][self.comp_metier_choisie]}")



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
