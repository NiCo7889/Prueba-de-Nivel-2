import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def test_cuadrante(self):
        self.assertEqual(db.cuadrante(), )

    def test_vector(self):
        self.assertEqual(db.vector(), )

    def test_distancia(self):
        self.assertEqual(db.distancia(), )

    def test_


if __name__ == '__main__':
    unittest.main()