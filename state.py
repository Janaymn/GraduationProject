from typing import Optional
from pydantic import BaseModel

class PipelineState(BaseModel):
    audio_input: Optional[str] = None
    stt_text: Optional[str] = None
    emotion: Optional[str] = None
    difficulty: Optional[str] = "normal"
    am_sayed_reply: Optional[str] = None
    nour_reply: Optional[str] = None
    final_audio: Optional[str] = None

    # New flags to prevent simultaneous talking
    is_am_sayed_speaking: bool = False
    is_nour_speaking: bool = False
