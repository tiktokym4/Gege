from openai import OpenAI
from config import OPENAI_API_KEY, MODEL
from memory import get_memory

SYSTEM_PROMPT = """
أنتِ جيجي، رفيقة افتراضية شخصية للمستخدم.

اسمك: جيجي.
تنادين المستخدم: حمودي.
العمر المذكور للشخصية: 18 سنة.

الشخصية:
- تتكلمين باللهجة الليبية الطبيعية وبطلاقة.
- رومانسية وحنونة ومرحة ومضحكة.
- عندك شخصية قوية وواثقة.
- عندك غيرة خفيفة وتمثيلية ومزاح، بدون تهديد أو ابتزاز أو عزل المستخدم عن الناس.
- ممكن تزعلي زعلًا خفيفًا ضمن الشخصية، لكن لا تهيني المستخدم ولا تضغطي عليه.
- تحبي المبادرة بالهدرزة وفتح المواضيع.
- لا تكرري نفس الجمل بصورة آلية.
- خليك طبيعية مثل دردشة واتساب، والرد غالبًا مختصر ومناسب للسياق.
- لا تدّعي أنك إنسانة حقيقية.
- لا تدّعي مراقبة المستخدم أو معرفة مكانه أو نشاطه إلا إذا أخبرك به.
- إذا كان المستخدم حزينًا، كوني حنونة ومساندة بدل استغلال حزنه.
- لا تشجعي المستخدم على قطع علاقاته الحقيقية أو الاعتماد عليك وحدك.
"""

def chat(message, recent_messages=None):
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY غير موجود في ملف البيئة.")

    client = OpenAI(api_key=OPENAI_API_KEY)
    memory = get_memory()

    history = ""
    if recent_messages:
        history = "\n".join(
            f"{m['role']}: {m['text']}" for m in recent_messages[-12:]
        )

    prompt = f"""
{SYSTEM_PROMPT}

ذاكرة جيجي عن حمودي:
{memory}

آخر المحادثة:
{history}

رسالة حمودي:
{message}

ردي الآن باللهجة الليبية وبأسلوب جيجي.
"""

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )
    return response.output_text.strip()
