# 💕 جيجي — النسخة الأولى

هذه نسخة أولى من عقل جيجي مع:
- شخصية ليبية
- ذاكرة محلية
- سجل محادثة SQLite
- Responses API
- Webhook لواتساب
- إرسال واستقبال الرسائل النصية

## التشغيل

1. انسخ `.env.example` إلى `.env`.
2. ضع مفتاح OpenAI في `OPENAI_API_KEY`.
3. ثبّت المتطلبات:
   `pip install -r requirements.txt`
4. شغّل:
   `python app.py`

## اختبار محلي

بعد التشغيل افتح:
`http://127.0.0.1:8080/`

## واتساب

تحتاج إعداد WhatsApp Business/Cloud API والحصول على:
- Access Token
- Phone Number ID
- Verify Token من اختيارك

ثم ضعها في `.env` واجعل رابط `/webhook` متاحًا عبر HTTPS.

لا تضع أي مفاتيح سرية داخل الكود أو ترسلها في المحادثة.
