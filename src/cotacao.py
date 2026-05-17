import requests


def obter_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    resposta = requests.get(url, timeout=10)

    dados = resposta.json()

    cotacao = float(dados["USDBRL"]["bid"])

    return cotacao