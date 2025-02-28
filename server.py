from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7589755463:AAE-vVUOARsSEZ4crfdd9_muUSS66tduXYM"  # Sostituisci con il tuo token
CHAT_ID = "-1002275165380"  # Sostituisci con il tuo chat ID

@app.route('/webhook', methods=['POST'])
def tradingview_webhook():
    data = request.json
    print("🔹 Webhook ricevuto:", data)  # Stampa i dati nei log di Render

    photo_url = data.get("photo")
    caption = data.get("caption", "📊 Trading Alert!")

    # Controlliamo se il link della foto è valido
    if "{{plot_url}}" in photo_url or photo_url is None:
        print("❌ Errore: URL immagine non valido!")
        return "Errore: URL immagine non valido", 400

    # Invia il messaggio a Telegram
    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    payload = {"chat_id": CHAT_ID, "photo": photo_url, "caption": caption}
    response = requests.post(telegram_url, json=payload)

    print("🔹 Telegram Response:", response.status_code, response.text)  # Stampa la risposta di Telegram

    return "Messaggio inviato!", 200 if response.status_code == 200 else f"Errore Telegram: {response.text}", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
