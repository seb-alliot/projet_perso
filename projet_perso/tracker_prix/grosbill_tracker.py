import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()


def grosbill_prix_tracker():
    url = "https://www.grosbill-pro.com/processeur/amd/50801.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
        "Accept-Language": "fr-FR,fr;q=0.9",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    prix_element = soup.find("h3", class_="gbpro_h1 gbpro_prix-haut")
    prix_cibler = prix_element.text.strip().replace("\xa0", "").replace(",", ".").replace("€", "")
    prix_courant = float(prix_cibler)
    return prix_courant
