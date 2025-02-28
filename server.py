from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7589755463:AAE-vVUOARsSEZ4crfdd9_muUSS66tduXYM"  # Sostituisci con il token del tuo bot Telegram
CHAT_ID = "-1002275165380"  # Sostituisci con il tuo chat ID o ID del gruppo

@app.route('/webhook', methods=['POST'])
def tradingview_webhook():
    data = request.json  # Riceve i dati da TradingView
    print("Webhook ricevuto:", data)

    photo_url = data.get("photo")
    caption = data.get("caption", "📊 Trading Alert!")

    # Invia l'immagine a Telegram
    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    payload = {"chat_id": CHAT_ID, "photo": photo_url, "caption": caption}
    response = requests.post(telegram_url, json=payload)

    return "Messaggio inviato!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
