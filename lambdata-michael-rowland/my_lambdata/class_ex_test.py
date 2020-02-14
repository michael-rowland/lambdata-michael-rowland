import unittest
from class_ex import Pitcher

class TestPitcher(unittest.TestCase):

    def test_wins(self):
        a_pitcher = Pitcher('Jose Berrios', 1, 17, 'R', 20, 30)
        self.assertEqual(a_pitcher.wins, 20)

if __name__ == '__main__':
    unittest.main()