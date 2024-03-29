from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"Cadena vacia")
    def test_sumar_unacadena(self):
          self.assertEqual(Calculadora().sumar("1"),1,"Un numero")


    def test_sumar_cadenaConUnNumero(self):
         self.assertEqual(Calculadora().sumar("1"),1,"Un número")
         self.assertEqual(Calculadora().sumar("2"), 2, "Un número")

    def test_sumar_cadenaConDosNumeros(self):
            self.assertEqual(Calculadora().sumar("1,3"),4,"Dos números")



    def test_sumar_cadenaConMultiplesNumeros(self):
        self.assertEqual(Calculadora().sumar("5","4","3","2","1"),12,""Multiples numero)
