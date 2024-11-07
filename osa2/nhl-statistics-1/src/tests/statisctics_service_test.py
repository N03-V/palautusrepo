import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytyy(self, name="Semenko"):
        pelaaja1 = self.stats.search(name) 
        pelaaja2 = Player("Semenko", "EDM", 4, 12)
        self.assertEqual(pelaaja1.name, pelaaja2.name)
        self.assertEqual(pelaaja1.team, pelaaja2.team)
        self.assertEqual(pelaaja1.goals, pelaaja2.goals)
        self.assertEqual(pelaaja1.assists, pelaaja2.assists)

    def test_search_ei_loydy(self, name="Matti"):
        pelaaja = self.stats.search(name) 
        self.assertEqual(pelaaja, None)

    def test_team(self, team_name="EDM"):
        tiimi1 = self.stats.team(team_name) 
        self.assertEqual(len(tiimi1), 3)
        self.assertEqual(tiimi1[0].name, "Semenko")
        self.assertEqual(tiimi1[1].name, "Kurri")
        self.assertEqual(tiimi1[2].name, "Gretzky")

        tiimi2 = self.stats.team("PIT") 
        self.assertEqual(len(tiimi2), 1)
        self.assertEqual(tiimi2[0].name, "Lemieux")

    def test_top(self, how_many=2):
        t = self.stats.top(how_many) 
        self.assertEqual(len(t), 3)
        self.assertEqual(t[0].name, "Gretzky")
        self.assertEqual(t[1].name, "Lemieux")
        self.assertEqual(t[2].name, "Yzerman")
