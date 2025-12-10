from typing import Optional, Dict, Any
from pydantic import BaseModel

class PipelineState(BaseModel):
    audio_input: Optional[str] = None
    stt_text: Optional[str] = None
    emotion: Optional[str] = None
    difficulty: Optional[str] = "normal"
    am_sayed_reply: Optional[str] = None
    nour_reply: Optional[str] = None
    final_audio: Optional[str] = None
