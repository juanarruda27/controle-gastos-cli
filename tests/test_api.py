import unittest
from unittest.mock import patch
from src.cotacao import obter_cotacao_dolar


class TestAPI(unittest.TestCase):

    @patch("src.cotacao.requests.get")
    def test_cotacao_dolar(self, mock_get):

        mock_get.return_value.json.return_value = {
            "USDBRL": {
                "bid": "5.50"
            }
        }

        cotacao = obter_cotacao_dolar()

        self.assertEqual(cotacao, 5.50)


if __name__ == "__main__":
    unittest.main()