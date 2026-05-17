import json
import os
from src.cotacao import obter_cotacao_dolar

FILE_NAME = "gastos.json"


def carregar_gastos():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def salvar_gastos(gastos):
    with open(FILE_NAME, "w") as f:
        json.dump(gastos, f, indent=4)


def adicionar_gasto(nome, valor):
    if valor < 0:
        raise ValueError("Valor não pode ser negativo")

    gastos = carregar_gastos()
    gastos.append({"nome": nome, "valor": valor})
    salvar_gastos(gastos)


def listar_gastos():
    gastos = carregar_gastos()
    return gastos


def total_gastos():
    gastos = carregar_gastos()
    return sum(g["valor"] for g in gastos)


def remover_gasto(indice):
    gastos = carregar_gastos()
    if indice < 0 or indice >= len(gastos):
        raise IndexError("Índice inválido")
    gastos.pop(indice)
    salvar_gastos(gastos)

def converter_para_dolar(total):
    cotacao = obter_cotacao_dolar()

    valor_dolar = total / cotacao

    print(f"Total em BRL: R$ {total:.2f}")
    print(f"Cotação atual: {cotacao}")
    print(f"Total em USD: $ {valor_dolar:.2f}")


def menu():
    while True:
        print("\n--- Controle de Gastos ---")
        print("1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Mostrar total")
        print("4. Remover gasto")
        print("5. Converter total para dólar")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do gasto: ")
            valor = float(input("Valor: "))
            adicionar_gasto(nome, valor)
            print("Gasto adicionado!")

        elif opcao == "2":
            gastos = listar_gastos()
            for i, g in enumerate(gastos):
                print(f"{i} - {g['nome']} | R$ {g['valor']}")

        elif opcao == "3":
            print(f"Total: R$ {total_gastos()}")

        elif opcao == "4":
            indice = int(input("Índice do gasto: "))
            remover_gasto(indice)
            print("Gasto removido!")
        
        elif opcao == "5":
            total = total_gastos()
            cotacao = obter_cotacao_dolar()
            print(f"Total em dólar: US$ {total / cotacao:.2f}")

        elif opcao == "6":
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()