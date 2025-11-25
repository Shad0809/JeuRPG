# src/personnage.py

class Personnage:
    def __init__(self, race=None, comp_race_auto=None, comp_race_choisie=None,
                 metier=None, comp_metier_auto=None, comp_metier_choisie=None):
        self.race = race
        self.metier = metier

        self.comp_race_auto = comp_race_auto
        self.comp_race_choisie = comp_race_choisie
        self.comp_metier_auto = comp_metier_auto
        self.comp_metier_choisie = comp_metier_choisie

        # Stats de base
        self.pv = 100
        self.attaque = 10
        self.vitesse = 10
        self.defense = 0

    def appliquer_bonus_optionnels(self, competences_race, competences_metier):
        """
        Calcule et applique les bonus de stats basés sur la compétence de race
        et la compétence de métier choisies.
        """
        # Réinitialiser les stats pour éviter l'accumulation lors de l'appel multiple
        self.pv = 100
        self.attaque = 10
        self.vitesse = 10
        self.defense = 0

        # Bonus race
        if self.comp_race_choisie and self.race in competences_race:
            bonus = competences_race[self.race].get(self.comp_race_choisie, {})
            self.pv += bonus.get("pv", 0)
            self.attaque += bonus.get("attaque", 0)
            self.vitesse += bonus.get("vitesse", 0)
            self.defense += bonus.get("defense", 0)

        # Bonus métier
        if self.comp_metier_choisie and self.metier in competences_metier:
            bonus = competences_metier[self.metier].get(self.comp_metier_choisie, {})
            self.pv += bonus.get("pv", 0)
            self.attaque += bonus.get("attaque", 0)
            self.vitesse += bonus.get("vitesse", 0)
            self.defense += bonus.get("defense", 0)

    def recap(self):
        """Retourne le récapitulatif des stats et choix du personnage."""
        return (f"Race : {self.race} ({self.comp_race_auto})\n"
                f"Compétence Race : {self.comp_race_choisie}\n"
                f"Métier : {self.metier} ({self.comp_metier_auto})\n"
                f"Compétence Métier : {self.comp_metier_choisie}\n\n"
                f"Vie (PV) : {self.pv}\n"
                f"Attaque : {self.attaque}\n"
                f"Vitesse : {self.vitesse}\n"
                f"Défense : {self.defense}")