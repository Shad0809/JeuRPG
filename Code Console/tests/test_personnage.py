import unittest
from personnage import Personnage
from competences import competence_raciale_auto, competence_metier_auto

class TestPersonnage(unittest.TestCase):

    def test_bonus_race(self):
        perso = Personnage(
            race="Gamer",
            comp_race_auto="Le Mode Rage",
            comp_race_choisie="Capture d'Écran",
            metier="Le Bio-Purificateur",
            comp_metier_auto="Purge Vitale",
            comp_metier_choisie="Le Nuage Désinfectant"
        )
        self.assertEqual(perso.attaque, 10 + 5)  # attaque +5 du bonus gamer

    def test_bonus_metier(self):
        perso = Personnage(
            race="Repugnant",
            comp_race_auto="Le Repoussoir Social",
            comp_race_choisie="Le Voile de Mouches",
            metier="Le Négociateur",
            comp_metier_auto="Manipulation de Valeur",
            comp_metier_choisie="Le Bon Deal"
        )
        self.assertEqual(perso.pv, 100 + 0 + 10)

if __name__ == "__main__":
    unittest.main()
