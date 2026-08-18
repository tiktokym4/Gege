from flask import Flask, request, jsonify
from config import WEBHOOK_VERIFY_TOKEN
from jiji import chat
from database import add_message, recent_messages
from whatsapp import send_text

app = Flask(__name__)

@app.get("/")
def home():
    return "💕 Jiji is running"

@app.get("/webhook")
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == WEBHOOK_VERIFY_TOKEN:
        return challenge or "", 200

    return "Forbidden", 403

@app.post("/webhook")
def receive_webhook():
    data = request.get_json(silent=True) or {}

    try:
        value = data["entry"][0]["changes"][0]["value"]
        messages = value.get("messages", [])

        for msg in messages:
            if msg.get("type") != "text":
                continue

            sender = msg["from"]
            incoming = msg["text"]["body"]

            add_message("user", incoming)
            reply = chat(incoming, recent_messages())
            add_message("assistant", reply)

            send_text(sender, reply)

    except (KeyError, IndexError, TypeError):
        # تجاهل الأحداث التي لا تحتوي رسالة نصية
        pass
    except Exception as exc:
        app.logger.exception("Webhook error: %s", exc)

    return jsonify({"ok": True}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
