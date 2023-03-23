import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def test_cuadrante(self):
        self.assertEqual(db.punto1.cuadrante(), None)

    def test_vector(self):
        self.assertEqual(db.punto1.vector(db.punto2), None)
        self.assertEqual(db.punto2.vector(db.punto1), None)

    def test_distancia(self):
        self.assertEqual(db.punto1.distancia(db.origen), None)
        self.assertEqual(db.punto2.distancia(db.origen), None)
        self.assertEqual(db.punto3.distancia(db.origen), None)

    def test_base(self):
        db.Rectangulo = db.rectangulo(db.punto1, db.punto2)
        self.assertEqual(db.Rectangulo.base(), None)
    
    def test_altura(self):
        db.Rectangulo = db.rectangulo(db.punto1, db.punto2)
        self.assertEqual(db.Rectangulo.altura(), None)

    def test_area(self):
        db.Rectangulo = db.rectangulo(db.punto1, db.punto2)
        self.assertEqual(db.Rectangulo.area(), None)

if __name__ == '__main__':
    unittest.main()