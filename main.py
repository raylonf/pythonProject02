# importar o App, Builder(GUI)
# criar o nosso aplicativo
# criar a função builder
import datetime

from kivy.app import App
from kivy.lang import Builder
import requests
from datetime import date

GUI = Builder.load_file("C:\\Users\\raylo\\PycharmProjects\\pythonProject02\\venv\\tela.kv")


class MeuAplicatitivo(App):
    def build(self):
        return GUI

    def on_start(self):
        cotacao_dolar= self.pegar_cotaçao("USD")
        cotacao_euro= self.pegar_cotaçao("EUR")
        cotacao_bitcoin= self.pegar_cotaçao("BTC")
        cotacao_ethereum= self.pegar_cotaçao("ETH")

        self.root.ids["datamoment"].text = f"Cotações do dia {date.today()}"
        self.root.ids["moeda1"].text = f"Dólar R$ {cotacao_dolar}"
        self.root.ids["moeda2"].text = f"Euro R$ {cotacao_euro}"
        self.root.ids["moeda3"].text = f"Bitcoin R$ {cotacao_bitcoin}"
        self.root.ids["moeda4"].text = f"Ethereum R$ {cotacao_ethereum}"

    def pegar_cotaçao(self, moeda):
        link= f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


MeuAplicatitivo().run()
