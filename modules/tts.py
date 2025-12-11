# modules/tts.py
from gtts import gTTS
from pydub import AudioSegment
import io

def tts_node(state):
    # Determine who should speak first based on flags
    if state.am_sayed_reply and not getattr(state, "is_nour_speaking", False):
        state.is_am_sayed_speaking = True
        full_text = state.am_sayed_reply

    elif state.nour_reply and not getattr(state, "is_am_sayed_speaking", False):
        state.is_nour_speaking = True
        full_text = state.nour_reply

    else:
        # No one is allowed to speak now
        return state

    # Generate TTS with gTTS (free, online)
    tts = gTTS(text=full_text, lang="ar")  # "ar" = Arabic

    # Save temporary MP3 in memory
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # Convert MP3 to WAV
    audio = AudioSegment.from_file(mp3_fp, format="mp3")
    audio.export("output3.wav", format="wav")

    state.final_audio = "output3.wav"

    # Reset speaking flags
    state.is_am_sayed_speaking = False
    state.is_nour_speaking = False

    return state
