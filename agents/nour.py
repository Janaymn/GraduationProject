# agents/nour.py
from langchain_groq import ChatGroq

groq = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)

NOUR_SYSTEM = """
انت نور، مساعدة مصرية بتساعد المستخدم ينجح في الموقف.
اتكلمي مصري فقط.
لو الحالة مش محتاجة تدخّل → قولي "".
"""

def nour_node(state):
    user = state.stt_text
    emotion = state.emotion
    am = state.am_sayed_reply

    prompt = f"""
    {NOUR_SYSTEM}

    المستخدم قال: "{user}"
    حالة المستخدم: {emotion}
    رد عم سيد: "{am}"

    هل تتدخلي؟
    لو نعم، قدمي تلميح صغير.
    لو لا، قولي "".
    """

    out = groq.invoke(prompt)
    state.nour_reply = out.content.strip()
    return state
