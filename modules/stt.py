# modules/stt.py
import ffmpeg
import os
from groq import Groq

client = Groq()

def convert_to_wav(input_file):
    output_file = "temp_input.wav"
    (
        ffmpeg.input(input_file)
        .output(output_file, format="wav", acodec="pcm_s16le", ac=1, ar="16000")
        .overwrite_output()
        .run(quiet=True)
    )
    return output_file

def stt_node(state):
    file = state.audio_input

    # Convert anything to wav before sending to Groq
    if not file.endswith(".wav"):
        file = convert_to_wav(file)

    # MUST pass file as binary object
    with open(file, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3",
            response_format="json",
            language="ar"
        )

    text = response.text.strip()
    state.stt_text = text
    return state
