import unittest
from main import TicTac

class TicTacGame_tasts(unittest.TestCase):

    def test_check_winner_1(self):
        self.assertEqual(TicTac.check_winner(self, ['X', 'X', 'X', 4, '0', 6, '0', 8, 9]), "Победил X!")
        self.assertEqual(TicTac.check_winner(self, ['0', '0', '0', 4, 'X', 'X', 'X', 8, 9]), "Победил 0!")
        self.assertEqual(TicTac.check_winner(self, ['0', '0', 3, 'X', 'X', 'X', 7, 8, 9]), "Победил X!")
        self.assertEqual(TicTac.check_winner(self, [1, 2, 3, '0', 5, '0', 'X', 'X', 'X']), "Победил X!")
        self.assertEqual(TicTac.check_winner(self, ['0', 2, 'X', 4, 'X', 6, 'X', '0', 9]), "Победил X!")
        self.assertEqual(TicTac.check_winner(self, ['X', 2, '0', 4, 'X', 6, '0', 8, 'X']), "Победил X!")
        self.assertEqual(TicTac.check_winner(self, ['X', 2, 'X', '0', '0', '0', 7, 8, 'X']), "Победил 0!")
        self.assertEqual(TicTac.check_winner(self, [1, 2, 'X', 4, 'X', 'X', '0', '0', '0']), "Победил 0!")
        self.assertEqual(TicTac.check_winner(self, ['X', 2, '0', 4, '0', 6, '0', 'X', 'X']), "Победил 0!")
        self.assertEqual(TicTac.check_winner(self, ['0', 2, 'X', 4, '0', 'X', 7, 'X', '0']), "Победил 0!")
        self.assertEqual(TicTac.check_winner(self, ['X', 'X', '0', '0', '0', 'X', 'X', 'X', '0']), False)

    def test_validate_input_1(self):
        self.assertEqual(TicTac.validate_input(self, 'sdadw'), False)
        self.assertEqual(TicTac.validate_input(self, 12), False)
        self.assertEqual(TicTac.validate_input(self, '2.5'), False)
        self.assertEqual(TicTac.validate_input(self, '2+2'), False)
        self.assertEqual(TicTac.validate_input(self, '11'), False)