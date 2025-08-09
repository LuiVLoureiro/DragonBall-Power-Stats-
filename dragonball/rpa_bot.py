from bs4 import BeautifulSoup as bs
from playwright.sync_api import sync_playwright
import string

# Personagem
# Nome
# Raça
# Técnicas
# Saga

class Bot():
    def __init__(self):
        for letra in string.ascii_uppercase:
            with sync_playwright() as p:
                navegador = p.chromium.launch(headless=False)
                pagina = navegador.new_page()
                pagina.goto(self.url(letra))
                

    def url(self, letter):
        base = f"https://dragonball.fandom.com/wiki/Category:Characters?from={letter}"
        return base

iniciar = Bot()