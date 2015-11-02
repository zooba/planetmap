from datetime import datetime
import vsop.planets
import unittest

# Test values obtained from http://neoprogrammics.com/vsop87/

class Test_vsop(unittest.TestCase):
    def test_mercury(self):
        p = vsop.planets.Mercury
        x, y, z = p.position_at(datetime(2000, 1, 1, 12))
        self.assertAlmostEqual(x, -0.1300934115)
        self.assertAlmostEqual(y, -0.4472876716)
        self.assertAlmostEqual(z, -0.0245983802)

        x, y, z = p.position_at(datetime(1899, 12, 31, 12))
        self.assertAlmostEqual(x, -0.3897246931)
        self.assertAlmostEqual(y, -0.1502242199)
        self.assertAlmostEqual(z, +0.0236199373)

        x, y, z = p.position_at(datetime(1799, 12, 30, 12))
        self.assertAlmostEqual(x, -0.1683565237)
        self.assertAlmostEqual(y, +0.2735108157)
        self.assertAlmostEqual(z, +0.0378103630)

    def test_venus(self):
        p = vsop.planets.Venus
        x, y, z = p.position_at(datetime(2000, 1, 1, 12))
        self.assertAlmostEqual(x, -0.7183022797)
        self.assertAlmostEqual(y, -0.0326546017)
        self.assertAlmostEqual(z, +0.0410142975)

        x, y, z = p.position_at(datetime(1899, 12, 31, 12))
        self.assertAlmostEqual(x, +0.6971428331)
        self.assertAlmostEqual(y, -0.2033631151)
        self.assertAlmostEqual(z, -0.0430201136)

        x, y, z = p.position_at(datetime(1799, 12, 30, 12))
        self.assertAlmostEqual(x, -0.5983535208)
        self.assertAlmostEqual(y, +0.3958502156)
        self.assertAlmostEqual(z, +0.0398238141)

    def test_earth(self):
        p = vsop.planets.Earth
        x, y, z = p.position_at(datetime(2000, 1, 1, 12))
        self.assertAlmostEqual(x, -0.1771354586)
        self.assertAlmostEqual(y, +0.9672416237)
        self.assertAlmostEqual(z, -0.0000039000)

        x, y, z = p.position_at(datetime(1899, 12, 31, 12))
        self.assertAlmostEqual(x, -0.1883079649)
        self.assertAlmostEqual(y, +0.9650688844)
        self.assertAlmostEqual(z, +0.0002150325)

        x, y, z = p.position_at(datetime(1799, 12, 30, 12))
        self.assertAlmostEqual(x, -0.1993918002)
        self.assertAlmostEqual(y, +0.9627974368)
        self.assertAlmostEqual(z, +0.0004307602)

    def test_mars(self):
        p = vsop.planets.Mars
        x, y, z = p.position_at(datetime(2000, 1, 1, 12))
        self.assertAlmostEqual(x, +1.3907159264)
        self.assertAlmostEqual(y, -0.0134157043)
        self.assertAlmostEqual(z, -0.0344677967)

        x, y, z = p.position_at(datetime(1899, 12, 31, 12))
        self.assertAlmostEqual(x, +0.4284332474)
        self.assertAlmostEqual(y, -1.3552354250)
        self.assertAlmostEqual(z, -0.0389650205)

        x, y, z = p.position_at(datetime(1799, 12, 30, 12))
        self.assertAlmostEqual(x, -1.1119219621)
        self.assertAlmostEqual(y, -1.0963263014)
        self.assertAlmostEqual(z, +0.0049208507)

    def test_jupiter(self):
        p = vsop.planets.Jupiter
        x, y, z = p.position_at(datetime(2000, 1, 1, 12))
        self.assertAlmostEqual(x, +4.0011740268)
        self.assertAlmostEqual(y, +2.9385810077)
        self.assertAlmostEqual(z, -0.1017837501)

        x, y, z = p.position_at(datetime(1899, 12, 31, 12))
        self.assertAlmostEqual(x, -3.0191224350)
        self.assertAlmostEqual(y, -4.4582563705)
        self.assertAlmostEqual(z, +0.0858641900)

        x, y, z = p.position_at(datetime(1799, 12, 30, 12))
        self.assertAlmostEqual(x, -0.0180390004)
        self.assertAlmostEqual(y, +5.1317748839)
        self.assertAlmostEqual(z, -0.0200448490)

    def test_saturn(self):
        p = vsop.planets.Saturn
        x, y, z = p.position_at(datetime(2000, 1, 1, 12))
        self.assertAlmostEqual(x, +6.4064068573)
        self.assertAlmostEqual(y, +6.5699929449)
        self.assertAlmostEqual(z, -0.3690768029)

        x, y, z = p.position_at(datetime(1899, 12, 31, 12))
        self.assertAlmostEqual(x, -0.36959737500)
        self.assertAlmostEqual(y, -10.0582398188)
        self.assertAlmostEqual(z, +0.19168543820)

        x, y, z = p.position_at(datetime(1799, 12, 30, 12))
        self.assertAlmostEqual(x, -5.6790910870)
        self.assertAlmostEqual(y, +7.1152478120)
        self.assertAlmostEqual(z, +0.0978521367)

    def test_uranus(self):
        p = vsop.planets.Uranus
        x, y, z = p.position_at(datetime(2000, 1, 1, 12))
        self.assertAlmostEqual(x, +14.4318934159)
        self.assertAlmostEqual(y, -13.7343162527)
        self.assertAlmostEqual(z, -0.23814219630)

        x, y, z = p.position_at(datetime(1899, 12, 31, 12))
        self.assertAlmostEqual(x, -6.48108333370)
        self.assertAlmostEqual(y, -17.8526893406)
        self.assertAlmostEqual(z, +0.01779352380)

        x, y, z = p.position_at(datetime(1799, 12, 30, 12))
        self.assertAlmostEqual(x, -18.2708335178)
        self.assertAlmostEqual(y, +0.98776557150)
        self.assertAlmostEqual(z, +0.24203442800)

    def test_neptune(self):
        p = vsop.planets.Neptune
        x, y, z = p.position_at(datetime(2000, 1, 1, 12))
        self.assertAlmostEqual(x, +16.8121116576)
        self.assertAlmostEqual(y, -24.9916630908)
        self.assertAlmostEqual(z, +0.12721901710)

        x, y, z = p.position_at(datetime(1899, 12, 31, 12))
        self.assertAlmostEqual(x, +1.51645574670)
        self.assertAlmostEqual(y, +29.8254538901)
        self.assertAlmostEqual(z, -0.64914002160)

        x, y, z = p.position_at(datetime(1799, 12, 30, 12))
        self.assertAlmostEqual(x, -20.3138943578)
        self.assertAlmostEqual(y, -22.4908255796)
        self.assertAlmostEqual(z, +0.93091515350)

if __name__ == '__main__':
    unittest.main()
