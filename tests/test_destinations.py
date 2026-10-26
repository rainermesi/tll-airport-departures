import unittest

from destinations import normalize_destination


class NormalizeDestinationTest(unittest.TestCase):
    def test_groups_same_airport_spellings(self):
        self.assertEqual(normalize_destination('Amsterdam'), 'Amsterdam')
        self.assertEqual(normalize_destination('Amsterdam - Schiphol'), 'Amsterdam')
        self.assertEqual(normalize_destination('Amsterdam (Schiphol)'), 'Amsterdam')
        self.assertEqual(normalize_destination('Geneva'), 'Genf')
        self.assertEqual(normalize_destination('Genf'), 'Genf')
        self.assertEqual(normalize_destination('Varssavi (Chopin)'), 'Varssavi')

    def test_keeps_distinct_airports(self):
        self.assertEqual(normalize_destination('London (Gatwick)'), 'London (Gatwick)')
        self.assertEqual(normalize_destination('London (Luton)'), 'London (Luton)')
        self.assertEqual(normalize_destination('Pariis (Orly)'), 'Pariis (Orly)')
        self.assertEqual(normalize_destination('Veneetsia-Treviso'), 'Veneetsia-Treviso')
        self.assertEqual(normalize_destination('Veneetsia (Marco Polo)'), 'Veneetsia')

    def test_normalizes_each_leg(self):
        self.assertEqual(
            normalize_destination('Stockholm (Arlanda),Pariis (Charles De Gaulle)'),
            'Stockholm (Arlanda),Pariis (Charles De Gaulle)',
        )
        self.assertEqual(normalize_destination('N/A'), 'N/A')


if __name__ == '__main__':
    unittest.main()
