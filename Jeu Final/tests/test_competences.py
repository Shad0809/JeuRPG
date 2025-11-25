import unittest
from src.competences import (competences_optionnelles_race, competences_optionnelles_metier,
                             competences_auto_race, competences_auto_metier)

class TestCompetences(unittest.TestCase):

    def test_comp_race_keys(self):
        for race, comps in competences_optionnelles_race.items():
            self.assertIsInstance(comps, dict)
            for comp, stats in comps.items():
                self.assertTrue(all(k in stats for k in ["pv", "attaque", "vitesse", "defense"]))

    def test_comp_metier_keys(self):
        for metier, comps in competences_optionnelles_metier.items():
            self.assertIsInstance(comps, dict)
            for comp, stats in comps.items():
                self.assertTrue(all(k in stats for k in ["pv", "attaque", "vitesse", "defense"]))

    def test_auto_comp_race(self):
        for race, comp in competences_auto_race.items():
            self.assertIsInstance(comp, str)

    def test_auto_comp_metier(self):
        for metier, comp in competences_auto_metier.items():
            self.assertIsInstance(comp, str)

if __name__ == "__main__":
    unittest.main()
