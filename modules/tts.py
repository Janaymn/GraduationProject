# modules/tts.py

from bark import SAMPLE_RATE, generate_audio
import soundfile as sf

def tts_node(state):
    full_text = state.am_sayed_reply

    if state.nour_reply:
        full_text = state.nour_reply + ". " + full_text

    audio_array = generate_audio(full_text)

    sf.write("output.wav", audio_array, SAMPLE_RATE)

    state.final_audio = "output.wav"
    return state
