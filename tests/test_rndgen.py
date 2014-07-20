#!/usr/local/bin/python3
import unittest
import unittest.mock
import sys

sys.path.append('..')
import rndgen

class test_rndgen_init(unittest.TestCase):
    """
    tests for verifing that drawing random cards works as expected
    """
    unsorted_state = [-2,-2,-2,-2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15]
    def setUp(self):
        self.deck = rndgen.RndGen()

    def tearDown(self):
        del self.deck

    def test_init_has_54_cards(self):
        self.assertEqual(len(self.deck.deck), 54)
        
    def test_init_has_correct_initial_state(self):
        self.deck.deck.sort()
        self.assertEqual(self.deck.deck,self.unsorted_state)   

    def test_drawing_a_card_removes_it_from_the_deck(self):
        self.deck.draw()
        self.assertEqual(len(self.deck.deck),53)
        
    def test_drawing_from_the_deck_wraps_arround(self):
        for i in range(54):
            self.deck.draw()
        self.deck.draw()
        self.assertEqual(len(self.deck.deck),53)

    def test_reset_deck(self):
        draw = [0,1,5,15,39,54]
        for draw_this_many_cards in draw:
            for i in range(draw_this_many_cards):
                self.deck.draw()
            self.deck.reset()
            self.assertEqual(len(self.deck.deck), 54)
            self.deck.deck.sort()
            self.assertEqual(self.deck.deck, self.unsorted_state)

    def test_draw_every_card(self):
        drawn = []
        for i in reversed(range(54)):
            drawn.append(self.deck.draw())
            self.assertEqual(self.deck.is_empty() , i == 0)
            self.assertEqual(len(self.deck.deck),i)
        drawn.sort()
        self.assertEqual(drawn,self.unsorted_state)
        self.assertEqual(self.deck.is_empty(), True)
        
if __name__ == '__main__':
    unittest.main()

