from datetime import datetime, timedelta
import vsop.util
import unittest

class Test_util(unittest.TestCase):
    def test_make_date(self):
        make_date = vsop.util._make_date
        self.assertEqual(make_date(2000), datetime(2000, 1, 1, 0, 0, 0))
        self.assertEqual(make_date(2000.0), datetime(2000, 1, 1, 0, 0, 0))
        self.assertEqual(make_date((2000, 2)), datetime(2000, 2, 1, 0, 0, 0))
        self.assertEqual(make_date((2000, 2, 3)), datetime(2000, 2, 3, 0, 0, 0))
        self.assertEqual(make_date((2000, 2, 3, 4)), datetime(2000, 2, 3, 4, 0, 0))
        self.assertEqual(make_date((2000, 2, 3, 4, 5)), datetime(2000, 2, 3, 4, 5, 0))
        self.assertEqual(make_date((2000, 2, 3, 4, 5, 6)), datetime(2000, 2, 3, 4, 5, 6))

    def test_daterange_day(self):
        daterange = vsop.util.daterange
        start, stop = datetime(2000, 1, 1), datetime(2001, 1, 1)
        
        days = list(daterange(start, stop, timedelta(days=1)))
        self.assertEqual(len(days), 366)
        day_delta = [(d2 - d1).days for d1, d2 in zip(days[:-1], days[1:])]
        self.assertSequenceEqual(day_delta, [1] * len(day_delta))

    def test_daterange_hour(self):
        daterange = vsop.util.daterange
        start, stop = datetime(2000, 1, 1), datetime(2000, 1, 2)
        
        hours = list(daterange(start, stop, timedelta(hours=1)))
        self.assertEqual(len(hours), 24)
        hours_delta = [(d2 - d1).total_seconds() for d1, d2 in zip(hours[:-1], hours[1:])]
        self.assertSequenceEqual(hours_delta, [3600] * len(hours_delta))

    def test_daterange_month(self):
        daterange = vsop.util.daterange
        start, stop = datetime(2000, 1, 1), datetime(2001, 1, 1)
        
        months = list(daterange(start, stop, step_months=1))
        self.assertEqual(len(months), 12)
        months_delta = [(d2 - d1).days for d1, d2 in zip(months[:-1], months[1:])]
        self.assertSequenceEqual(months_delta, [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30])

    def test_daterange_year(self):
        daterange = vsop.util.daterange
        start, stop = datetime(2000, 1, 1), datetime(2010, 1, 1)
        
        years = list(daterange(start, stop, step_years=1))
        self.assertEqual(len(years), 10)
        years_delta = [(d2 - d1).days for d1, d2 in zip(years[:-1], years[1:])]
        self.assertSequenceEqual(years_delta, [366, 365, 365, 365, 366, 365, 365, 365, 366])

if __name__ == '__main__':
    unittest.main()
