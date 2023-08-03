import streamlit.components.v1 as components

_voice_recorder = components.declare_component(
    "voice_recorder",
    url="http://localhost:3001",
)

def voice_recorder():
    recording = _voice_recorder()
    return recording
