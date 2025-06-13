import unittest
import product

class TestProduct(unittest.TestCase):
    def test_create(self):
        p = product.Product("MINT", 100, 5.6)
        self.assertEqual(p.name , "MINT")
        self.assertEqual(p.quant, 100)
        self.assertEqual(p.price, 5.6)

    def test_bad_quant(self):
        p = product.Product("MINT", 100, 5.6)
        with self.assertRaises(TypeError):
            p.quant = "ten"

if __name__ == "__main__":
    unittest.main()