import requests


def obter_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    resposta = requests.get(url, timeout=10)

    dados = resposta.json()

    if "USDBRL" not in dados:
        raise Exception("Erro ao obter cotação da API")

    cotacao = float(dados["USDBRL"]["bid"])

    return cotacao