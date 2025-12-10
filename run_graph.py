from graph import app
from state import PipelineState

state = PipelineState(
    audio_input="user_audio.webm"
)

final = app.invoke(state)
print("Generated audio:", final["final_audio"])
