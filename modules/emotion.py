# modules/emotion.py
from langchain_groq import ChatGroq

groq = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def emotion_node(state):
    prompt = f"""
    Classify the emotion of the speaker from this text:
    "{state.stt_text}"

    Valid labels:
    calm, neutral, confused, stressed, panicking
    """

    out = groq.invoke(prompt)
    state.emotion = out.content.strip().lower()
    return state
