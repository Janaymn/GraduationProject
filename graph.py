from langgraph.graph import StateGraph
from state import PipelineState
from modules.stt import stt_node
from modules.emotion import emotion_node
from modules.difficulty import difficulty_node
from agents.am_sayed import am_sayed_node
from agents.nour import nour_node
from modules.tts import tts_node

graph = StateGraph(PipelineState)

graph.add_node("stt", stt_node)
graph.add_node("emotion", emotion_node)
graph.add_node("difficulty", difficulty_node)
graph.add_node("am_sayed", am_sayed_node)
graph.add_node("nour", nour_node)
graph.add_node("tts", tts_node)

graph.set_entry_point("stt")
graph.add_edge("stt", "emotion")
graph.add_edge("emotion", "difficulty")
graph.add_edge("difficulty", "am_sayed")
graph.add_edge("am_sayed", "nour")
graph.add_edge("nour", "tts")

app = graph.compile()
