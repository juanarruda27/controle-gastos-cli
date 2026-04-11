import os
import unittest
from src.app import adicionar_gasto, listar_gastos, total_gastos, remover_gasto

ARQUIVO_TESTE = "gastos.json"


class TestControleGastos(unittest.TestCase):

    def setUp(self):
        # limpa arquivo antes de cada teste
        if os.path.exists(ARQUIVO_TESTE):
            os.remove(ARQUIVO_TESTE)

    def test_adicionar_gasto(self):
        adicionar_gasto("Lanche", 10)
        gastos = listar_gastos()
        self.assertEqual(len(gastos), 1)
        self.assertEqual(gastos[0]["nome"], "Lanche")

    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            adicionar_gasto("Erro", -5)

    def test_total_gastos(self):
        adicionar_gasto("A", 10)
        adicionar_gasto("B", 20)
        self.assertEqual(total_gastos(), 30)

    def test_remover_gasto(self):
        adicionar_gasto("A", 10)
        remover_gasto(0)
        self.assertEqual(len(listar_gastos()), 0)

    def test_indice_invalido(self):
        with self.assertRaises(IndexError):
            remover_gasto(0)


if __name__ == "__main__":
    unittest.main()