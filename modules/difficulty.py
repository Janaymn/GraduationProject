# modules/difficulty.py
def difficulty_node(state):
    emo = state.emotion
    if emo in ["stressed", "panicking"]:
        state.difficulty = "easy"
    elif emo == "confused":
        state.difficulty = "normal"
    else:
        state.difficulty = "hard"
    return state

