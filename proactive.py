from datetime import datetime, timedelta
import random

TOPICS = [
    "شن أكثر حاجة ضحكتك اليوم؟ 😂",
    "حمودي، عندي سؤال فضولي عليك 👀",
    "تعال نهدرزوا شوية، شن أخبارك اليوم؟ ❤️",
    "لو خيرتك بين طلعة وقعدة هادية في البيت، شن تختار؟",
    "عندي موضوع بنختلفوا عليه غالبًا 😂"
]

def should_initiate(last_activity_iso, minimum_hours=4):
    if not last_activity_iso:
        return True
    try:
        last = datetime.fromisoformat(last_activity_iso)
    except ValueError:
        return False
    return datetime.utcnow() - last >= timedelta(hours=minimum_hours)

def proactive_message():
    return random.choice(TOPICS)
