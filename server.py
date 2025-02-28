from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7589755463:AAE-vVUOARsSEZ4crfdd9_muUSS66tduXYM"  # Sostituisci con il token del tuo bot
CHAT_ID = "-1002275165380"  # Sostituisci con il tuo chat ID

@app.route('/webhook', methods=['POST'])
def tradingview_webhook():
    try:
        data = request.json  # Riceve i dati da TradingView
        print("🔹 Webhook ricevuto:", data)  # Stampa i dati nei log di Render

        if not data or not isinstance(data, dict):  # Controlla se i dati sono validi
            print("❌ Errore: Nessun JSON valido ricevuto!")
            return "Errore: Nessun JSON valido ricevuto", 400

        # Ottieni il link dell'immagine e la caption
        photo_url = data.get("photo", "").strip()
        caption = data.get("caption", "📊 Trading Alert!")

        # Controlliamo se `photo_url` è valido
        if not photo_url or "{{plot_url}}" in photo_url:
            print("❌ Errore: URL immagine non valido!")
            return "Errore: URL immagine non valido", 400

        # Invia il messaggio a Telegram
        telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        payload = {"chat_id": CHAT_ID, "photo": photo_url, "caption": caption}

        response = requests.post(telegram_url, json=payload)
        print("🔹 Telegram Response:", response.status_code, response.text)  # Stampa la risposta di Telegram

        if response.status_code == 200:
            return "Messaggio inviato!", 200
        else:
            return f"Errore Telegram: {response.text}", 400

    except Exception as e:
        print(f"❌ Errore Generale: {str(e)}")
        return f"Errore Generale: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
