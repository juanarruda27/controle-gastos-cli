import unittest
from src.cotacao import obter_cotacao_dolar


class TestAPI(unittest.TestCase):

    def test_cotacao_dolar(self):
        cotacao = obter_cotacao_dolar()

        self.assertIsInstance(cotacao, float)
        self.assertGreater(cotacao, 0)


if __name__ == "__main__":
    unittest.main()