import unittest
from card import Card

class MyTestCase(unittest.TestCase):

    def test_ranks_equal(self):
        self.assertEqual(Card('10', "DIAMONDS"), Card('10', "SPADES"))
        self.assertEqual(Card('J', "DIAMONDS"), Card('J', "HEARTS"))
        self.assertEqual(Card('Q', "HEARTS"), Card('Q', "SPADES"))
        self.assertEqual(Card('A', "DIAMONDS"), Card('A', "CLUBS"))
        self.assertEqual(Card('K', "CLUBS"), Card('K', "SPADES"))

    def test_ranks_not_equal(self):
        self.assertNotEqual(Card('10', "DIAMONDS"), Card('J', "SPADES"))
        self.assertNotEqual(Card('J', "DIAMONDS"), Card('Q', "HEARTS"))
        self.assertNotEqual(Card('Q', "HEARTS"), Card('A', "SPADES"))
        self.assertNotEqual(Card('A', "DIAMONDS"), Card('K', "CLUBS"))
        self.assertNotEqual(Card('K', "CLUBS"), Card('10', "SPADES"))
        self.assertNotEqual(Card('A', "DIAMONDS"), Card('J', "SPADES"))
        self.assertNotEqual(Card('K', "DIAMONDS"), Card('Q', "HEARTS"))
        self.assertNotEqual(Card('J', "HEARTS"), Card('A', "SPADES"))
        self.assertNotEqual(Card('10', "DIAMONDS"), Card('K', "CLUBS"))
        self.assertNotEqual(Card('Q', "CLUBS"), Card('10', "SPADES"))

    def test_ranks_greater_than(self):
        self.assertGreater(Card('J', "DIAMONDS"), Card('10', "SPADES"))
        self.assertGreater(Card('Q', "DIAMONDS"), Card('10', "SPADES"))
        self.assertGreater(Card('K', "DIAMONDS"), Card('10', "SPADES"))
        self.assertGreater(Card('A', "DIAMONDS"), Card('10', "SPADES"))
        self.assertGreater(Card('Q', "DIAMONDS"), Card('J', "SPADES"))
        self.assertGreater(Card('K', "DIAMONDS"), Card('J', "SPADES"))
        self.assertGreater(Card('A', "DIAMONDS"), Card('J', "SPADES"))
        self.assertGreater(Card('K', "DIAMONDS"), Card('Q', "SPADES"))
        self.assertGreater(Card('A', "DIAMONDS"), Card('Q', "SPADES"))
        self.assertGreater(Card('A', "DIAMONDS"), Card('K', "SPADES"))

    def test_ranks_less_than(self):
        self.assertLess(Card('10', "DIAMONDS"), Card('J', "SPADES"))
        self.assertLess(Card('J', "DIAMONDS"), Card('Q', "HEARTS"))
        self.assertLess(Card('Q', "HEARTS"), Card('K', "SPADES"))
        self.assertLess(Card('K', "CLUBS"), Card('A', "DIAMONDS"))
        self.assertLess(Card('10', "CLUBS"), Card('Q', "SPADES"))

    def test_ranks_greater_than_or_equal(self):
        self.assertGreaterEqual(Card('J', "DIAMONDS"), Card('10', "SPADES"))
        self.assertGreaterEqual(Card('Q', "DIAMONDS"), Card('Q', "HEARTS"))
        self.assertGreaterEqual(Card('A', "DIAMONDS"), Card('K', "CLUBS"))
        self.assertGreaterEqual(Card('10', "SPADES"), Card('10', "DIAMONDS"))

    def test_ranks_less_than_or_equal(self):
        self.assertLessEqual(Card('10', "DIAMONDS"), Card('J', "SPADES"))
        self.assertLessEqual(Card('Q', "HEARTS"), Card('Q', "SPADES"))
        self.assertLessEqual(Card('K', "CLUBS"), Card('A', "DIAMONDS"))
        self.assertLessEqual(Card('A', "CLUBS"), Card('A', "DIAMONDS"))

    def test_card_creation(self):
        card = Card('7', "CLUBS")
        self.assertEqual(card.rank, '7')
        self.assertEqual(card.suit, "CLUBS")

        card = Card('A', "HEARTS")
        self.assertEqual(card.rank, 'A')
        self.assertEqual(card.suit, "HEARTS")

    def test_card_representation(self):
        card = Card('Q', "SPADES")
        self.assertEqual(str(card), 'Q♠')

        card = Card('10', "DIAMONDS")
        self.assertEqual(str(card), '10◆')

if __name__ == '__main__':
    unittest.main()