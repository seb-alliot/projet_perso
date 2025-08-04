import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
from email.message import EmailMessage
import time
EMAIL = os.getenv('EMAIL')
MDP = os.getenv('MDP')

def comparateur_prix():
    from amazon_tracker import amazon_prix_tracker
    from grosbill_tracker import grosbill_prix_tracker

    prix_minimum, prix_maximum = 200.0, 220.0
    prix_connu= []

    while True:
        try:
            prix_existant = False
            site = {
                "amazon": {
                    "prix": amazon_prix_tracker()
                },
                "grosbill": {
                    "prix": grosbill_prix_tracker()
                }
            }

            for nom_site, prix_trouver in site.items():
                if (nom_site, prix_trouver['prix']) in prix_connu:
                    continue
                if prix_trouver['prix'] is None:
                    continue
                prix_connu.append((nom_site, prix_trouver['prix']))
                prix_existant = True
            site_moins_cher = min(site.items(), key=lambda x: x[1]['prix'])
            site_moins_cher = f"Le prix le moins cher est sur {site_moins_cher[0]} : {site_moins_cher[1]['prix']} €"

            if prix_minimum <= site['amazon']['prix'] <= prix_maximum or prix_minimum <= site['grosbill']['prix'] <= prix_maximum:
                msg = EmailMessage()
                msg.set_content(f"{site_moins_cher}")
                msg['Subject'] = 'Alerte Prix'
                msg['From'] = EMAIL
                msg['To'] = EMAIL

                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.starttls()
                    smtp.login(EMAIL, MDP)
                    smtp.send_message(msg)
            if not prix_existant:
                time.sleep(3600)
        except Exception as e:
                    print(f"Erreur lors de l'envoi de l'email : {e}")
comparateur_prix()