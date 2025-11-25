# tests/test_personnage.py (CORRIGÉ)

import unittest
from src.personnage import Personnage
from src.competences import competences_optionnelles_race, competences_optionnelles_metier


class TestPersonnage(unittest.TestCase):

    def setUp(self):
        # Définition des dictionnaires pour les rendre disponibles dans tous les tests
        self.race_comps = competences_optionnelles_race
        self.metier_comps = competences_optionnelles_metier

    def test_stats_initiales(self):
        p = Personnage()
        self.assertEqual(p.pv, 100)
        self.assertEqual(p.attaque, 10)
        self.assertEqual(p.vitesse, 10)
        self.assertEqual(p.defense, 0)

    def test_bonus_race(self):
        # 1. Initialiser le personnage avec les choix
        p = Personnage(race="Répugnant", comp_race_choisie="L'Odeur de la Crainte",
                       metier="BioPurificateur", comp_metier_choisie="comp1")

        # 2. Appliquer les bonus explicitement (comme dans main.py)
        p.appliquer_bonus_optionnels(self.race_comps, self.metier_comps)  # <--- NOUVEAU

        bonus_race = self.race_comps["Répugnant"]["L'Odeur de la Crainte"]
        bonus_metier = self.metier_comps["BioPurificateur"]["comp1"]

        # 3. Vérifier les résultats
        expected_pv = 100 + bonus_race["pv"] + bonus_metier["pv"]
        expected_attaque = 10 + bonus_race["attaque"] + bonus_metier["attaque"]
        expected_vitesse = 10 + bonus_race["vitesse"] + bonus_metier["vitesse"]
        expected_defense = 0 + bonus_race["defense"] + bonus_metier["defense"]

        self.assertEqual(p.pv, expected_pv)
        self.assertEqual(p.attaque, expected_attaque)
        self.assertEqual(p.vitesse, expected_vitesse)
        self.assertEqual(p.defense, expected_defense)

    def test_appliquer_bonus_separement(self):
        p = Personnage()
        p.race = "Gamer"
        p.comp_race_choisie = "Le Speedrun Tactique"
        p.metier = "Mastodonte"
        p.comp_metier_choisie = "comp1"

        # CORRECTION du TypeError : Passer les 2 arguments requis
        p.appliquer_bonus_optionnels(self.race_comps, self.metier_comps)  # <--- CORRIGÉ

        bonus_race = self.race_comps["Gamer"]["Le Speedrun Tactique"]
        bonus_metier = self.metier_comps["Mastodonte"]["comp1"]

        # Vérifier les résultats
        expected_pv = 100 + bonus_race["pv"] + bonus_metier["pv"]
        expected_attaque = 10 + bonus_race["attaque"] + bonus_metier["attaque"]
        expected_vitesse = 10 + bonus_race["vitesse"] + bonus_metier["vitesse"]
        expected_defense = 0 + bonus_race["defense"] + bonus_metier["defense"]

        self.assertEqual(p.pv, expected_pv)
        self.assertEqual(p.attaque, expected_attaque)
        self.assertEqual(p.vitesse, expected_vitesse)
        self.assertEqual(p.defense, expected_defense)


if __name__ == "__main__":
    unittest.main()