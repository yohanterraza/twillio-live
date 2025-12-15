from twilio.rest import Client
import time

# ⚠️ Remplace par tes identifiants Twilio
account_sid = 'US8cd7018a24db072ed7acf43cb32de1d1'
auth_token = '3a15a00b08139ab2b12eff1e60f5583d'
from_number = '+18777804236'  # Ton numéro Twilio

client = Client(account_sid, auth_token)

# URL publique de ton TwiML
twiml_url = 'https://yohanterraza.github.io/twillio-live/twiml.xml'

# Liste des numéros à appeler
numeros = [
    '+330658085908',
    '+41797825096'
]

for numero in numeros:
    try:
        call = client.calls.create(
            to=numero,
            from_=from_number,
            url=twiml_url
        )
        print(f"Appel lancé vers {numero}, SID: {call.sid}")
        time.sleep(2)  # pause 2 secondes entre les appels
    except Exception as e:
        print(f"Erreur pour {numero} : {e}")

