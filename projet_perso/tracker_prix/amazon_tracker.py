import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()


def amazon_prix_tracker():
    url = "https://www.amazon.fr/AMD-Ryzen-9-5950X-RyzenTM/dp/B0815Y8J9N/ref=sr_1_1?dib=eyJ2IjoiMSJ9.wxxTaq5QGDP3nGxP6Lm18QI3ygkGRyOHsXUDymlq8JI6Vx6XRo4D2eB2NJ39cNTs9K9V77mkL1THxPqO6vd96E470K_0gtRybdLayYaCzBSUdaK1eVObPblRawrDhBR0NMrGVW1XYIYlwrEGbcIc8DquRhto6_0qFk3sQR14X7e4Zb0HnP5spahsFA-m0UIc6N493fCug4uBkkzikMgRBGDQxxiZGJYpPPnavMc9CHuK6_xXp0bAo_CtBtsOzLsdJsOAcdbHUzfp_vLD1WFj2H74t97V2y8VwV4MYjSIDeg.44UaQzANXOEXlrcnwVqcYpyAF9_LYrQNxM0uWcuLGB4&dib_tag=se&keywords=5950x&qid=1754171134&sr=8-1&th=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
        "Accept-Language": "fr-FR,fr;q=0.9",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    prix_element = soup.find("span", {"class": "a-price-whole"})
    prix_courant = float(prix_element.text.strip().replace("\xa0", "").replace(",", ".").replace("€", ""))
    print(f"Prix actuel sur Amazon : {prix_courant} €")
    return prix_courant
