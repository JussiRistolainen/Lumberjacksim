from fitem import Item
from fposition import Position
import pygame
import unittest
import math


class TestPositionMethods(unittest.TestCase):

    position1 = Position(2, 3)
    position2 = Position(5, 4)
    position3 = position2

    def test_posX(self):
        self.assertEqual(self.position1.getPositionX(), 2)
        self.assertEqual(self.position2.getPositionX(), 5)
        self.assertEqual(self.position3.getPositionX(), 5)

    def test_posY(self):
        self.assertEqual(self.position1.getPositionY(), 3)
        self.assertEqual(self.position2.getPositionY(), 4)
        self.assertEqual(self.position3.getPositionY(), 4)

    def test_distanceFromPos(self):
        position4 = Position(1, 4)
        position5 = Position(-1, 5)

        self.assertAlmostEqual(
            self.position1.getDistanceFromPosition(position4),
            math.sqrt((2 - 1) * (2 - 1) + (3 - 4) * (3 - 4)),
        )
        self.assertAlmostEqual(
            self.position1.getDistanceFromPosition(position5),
            math.sqrt((2 + 1) * (2 + 1) + (3 - 5) * (3 - 5)),
        )

        self.assertAlmostEqual(
            self.position2.getDistanceFromPosition(position4),
            math.sqrt((5 - 1) * (5 - 1) + (4 - 4) * (4 - 4)),
        )
        self.assertAlmostEqual(
            self.position2.getDistanceFromPosition(position5),
            math.sqrt((5 + 1) * (5 + 1) + (4 - 5) * (4 - 5)),
        )

        self.assertAlmostEqual(
            self.position3.getDistanceFromPosition(position4),
            math.sqrt((5 - 1) * (5 - 1) + (4 - 4) * (4 - 4)),
        )
        self.assertAlmostEqual(
            self.position3.getDistanceFromPosition(position5),
            math.sqrt((5 + 1) * (5 + 1) + (4 - 5) * (4 - 5)),
        )


if __name__ == "__main__":
    unittest.main()