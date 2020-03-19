from asynctest import TestCase

from example import Calculadora


class CalculadoraTest(TestCase):
    async def test_min(self):
        calc = Calculadora()
        self.assertEqual(10, calc.min(10, 20))
        self.assertEqual(10, calc.min(20, 10))
        self.assertEqual(-10, calc.min(-1, -10))
        self.assertEqual(-1, calc.min(-1, 0))

    async def test_max(self):
        calc = Calculadora()
        self.assertEqual(20, calc.max(10, 20))
        self.assertEqual(20, calc.max(20, 10))
        self.assertEqual(-1, calc.max(-1, -10))
        self.assertEqual(0, calc.max(-1, 0))

    async def test_abs(self):
        calc = Calculadora()
        self.assertEqual(20, calc.abs(-20))
        self.assertEqual(20, calc.abs(20))
        self.assertEqual(0, calc.abs(-0))
