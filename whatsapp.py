import requests
from config import WHATSAPP_ACCESS_TOKEN, WHATSAPP_PHONE_NUMBER_ID, GRAPH_API_VERSION

def send_text(to, text):
    if not WHATSAPP_ACCESS_TOKEN or not WHATSAPP_PHONE_NUMBER_ID:
        raise RuntimeError("بيانات WhatsApp API غير موجودة.")

    url = (
        f"https://graph.facebook.com/{GRAPH_API_VERSION}/"
        f"{WHATSAPP_PHONE_NUMBER_ID}/messages"
    )

    headers = {
        "Authorization": f"Bearer {WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()
