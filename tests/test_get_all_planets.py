import unittest
import service

class Test_get_all_planets(unittest.TestCase):
    def test_all_planets(self):
        res = service.get_all_planets(2015, 10, 6)
        self.assertIn("mercury", res.keys())
        self.assertIn("venus", res.keys())
        self.assertIn("earth", res.keys())
        self.assertIn("mars", res.keys())
        self.assertIn("jupiter", res.keys())
        self.assertIn("saturn", res.keys())
        self.assertIn("uranus", res.keys())
        self.assertIn("neptune", res.keys())
        self.assertIn("pluto", res.keys())

    def test_invalid_date(self):
        res = service.get_all_planets(2015, 02, 29)
        # Invalid date should return a complete set of planets
        # with (0., 0., 0.) for all coordinates.
        self.assertSetEqual(
            {"mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"},
            set(res.keys())
        )
        self.assertTrue(all(v == (0., 0., 0.) for v in res.values()))

if __name__ == '__main__':
    unittest.main()
