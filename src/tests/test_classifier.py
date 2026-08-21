# test_classifier.py — Pruebas unitarias

import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from clasificador import classify_ticket

class TestClassifier(unittest.TestCase):

    def test_hardware(self):
        result = classify_ticket("Mi impresora no funciona")
        self.assertEqual(result["category"], "Hardware")
        self.assertEqual(result["priority"], "Alta")

    def test_software(self):
        result = classify_ticket("El programa da error al abrir")
        self.assertEqual(result["category"], "Software")
        self.assertEqual(result["priority"], "Media")

    def test_red(self):
        result = classify_ticket("No tengo internet desde ayer")
        self.assertEqual(result["category"], "Red")
        self.assertEqual(result["priority"], "Alta")

    def test_acceso(self):
        result = classify_ticket("Olvide mi contraseña")
        self.assertEqual(result["category"], "Acceso")
        self.assertEqual(result["priority"], "Media")

    def test_general(self):
        result = classify_ticket("Tengo un problema raro")
        self.assertEqual(result["category"], "General")
        self.assertEqual(result["priority"], "Baja")

if __name__ == "__main__":
    unittest.main()
