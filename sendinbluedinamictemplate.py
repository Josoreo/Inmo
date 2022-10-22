import requests

def send_email(nombre, deuda, mail):

    url = "https://api.sendinblue.com/v3/smtp/email"

    payload = {
        "sender": {
            "name": "Patagonica",
            "email": "jhpueyrredon@gmail.com"
        },
        "to": [
            {
                "email": mail,
                "name": nombre
            }
        ],
        "params": {
            "nombre": nombre,
            "deuda": deuda
        },
        "subject": "A pagar",
        "templateId": 2
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "api-key": "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"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


