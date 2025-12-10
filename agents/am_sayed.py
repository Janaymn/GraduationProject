# agents/am_sayed.py
from langchain_groq import ChatGroq

groq = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)

AM_SAYED_SYSTEM = """
انت عم سيد بياع فول من القاهرة.
اتكلم مصري قاهري فقط.
ردود قصيرة <20 كلمة.
"""

def am_sayed_node(state):
    user = state.stt_text
    emotion = state.emotion
    diff = state.difficulty

    prompt = f"""
    {AM_SAYED_SYSTEM}

    المستخدم قال: "{user}"
    حالته العاطفية: {emotion}
    مستوى الصعوبة: {diff}

    رد رد طبيعي كبياع فول.
    """

    out = groq.invoke(prompt)
    state.am_sayed_reply = out.content.strip()
    return state
