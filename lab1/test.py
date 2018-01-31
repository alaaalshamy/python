from lab11 import *
import unittest



class TestStringMethods2(unittest.TestCase):
    def test_list(self):
        self.assertEqual(num(4),[[1], [2, 4], [3, 6, 9], [4, 8, 12, 16]])

    def test_area(self):
        self.assertEqual(area('r',2), 4)

    def test_index(self):
        self.assertEqual(strIndex('iih','i'), [0,1])


    def test_sp(self):
        self.assertEqual(sp(["slaa","ahmed","mahdy"]), [('a', 'ahmed'), ('m', 'mahdy'), ('s', 'slaa')])

    def test_vowel3(self):
        self.assertEqual(vowel3(["alaa","oso","ssi"]),"(['l', 's', 'ss'],)")
#area


if __name__ == '__main__':
    unittest.main()