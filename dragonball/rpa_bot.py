from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import string

# Personagem [x]
# Nome [x]
# Raça [x]
# Técnicas []
# Saga []

class Bot():
    def __init__(self):
        characters_url = "wiki/Category:Characters?from="
        for letra in string.ascii_uppercase:
            with sync_playwright() as p:
                navegador = p.chromium.launch(headless=True)
                pagina = navegador.new_page()
                pagina.goto(self.url(characters_url, letra))
                soup = BeautifulSoup(pagina.content(), "html.parser")
                nomes = soup.find_all("a", class_="category-page__member-link")
                
                for nome in nomes: 
                    # Tratamento dos Nomes
                    if "Category" not in nome.text[0:9]:
                        # Nomes
                        print(nome.text)
                        # Links 
                        link_character = nome.get("href")
                        pagina.goto(self.url(link_character, ""))
                        soup = BeautifulSoup(pagina.content(), "html.parser")
                        # Raça
                        raça = soup.find_all("div", {"data-source": "Race"})
                        for i in raça:
                            raça = i.find("div", class_="pi-data-value pi-font").text
                        
                    else:
                        pass


        
        # Extrair os Nomes e Links por página
        # Extrair Técnicas e Saga por Nome




    def url(self, context, letter):
        base = f"https://dragonball.fandom.com/{context}{letter}"
        return base

iniciar = Bot() 