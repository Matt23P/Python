import unittest
import main


class TestCase(unittest.TestCase):
    def test_findDuplicates(self):
        lista1 = [1, 1, 6, 5, 7, 11, 7, 3, 3, 3, 9, None, 8]
        lista2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        lista3 = [8, 2, 4, 6, 1, 3, 5, 9, 5, 12, 5, 5, 12, 3, 2, 2]
        lista4 = [None, None, None, None]
        lista5 = [2, 2, 4, 5, 1, 2, 5, 7, 8, 5, 9, 9, 9, 0, 1]
        wynik1 = main.findDuplicates(lista1, 2)
        wynik2 = main.findDuplicates(lista2, 6)
        wynik3 = main.findDuplicates(lista3, 4)
        wynik4 = main.findDuplicates(lista4, 4)
        wynik5 = main.findDuplicates(lista5, 3)

        self.assertEqual(len(wynik1), 2)
        self.assertEqual(wynik1.pop(), 7)
        self.assertEqual(wynik1.pop(), 1)

        self.assertEqual(len(wynik2), 0)

        self.assertEqual(len(wynik3), 1)
        self.assertEqual(wynik3.pop(), 5)

        self.assertEqual(len(wynik4), 0)

        self.assertEqual(len(wynik5), 3)
        self.assertEqual(wynik5.pop(), 9)
        self.assertEqual(wynik5.pop(), 5)
        self.assertEqual(wynik5.pop(), 2)



if __name__ == '__main__':
    unittest.main()
