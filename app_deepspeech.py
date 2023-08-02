import streamlit as st
import sounddevice as sd
import numpy as np
import speech_recognition as sr

def record_audio(duration=5, sample_rate=44100):
    st.write("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    return audio_data

def speech_to_text(language="en-US"):
    audio_data = record_audio()
    audio_data = np.squeeze(audio_data)
    audio_bytes = audio_data.tobytes()

    r = sr.Recognizer()

    try:
        st.write("Transcription:")
        text = r.recognize_google(audio_bytes, language=language)
        st.write(text)
    except sr.UnknownValueError:
        st.error("Sorry, could not understand audio.")
    except sr.RequestError as e:
        st.error("Error fetching results from Google Speech Recognition service; {0}".format(e))

def main():
    st.title("Speech-to-Text Converter")
    st.write("Select the language and start speaking.")

    language = st.selectbox("Select Language", ["en-US", "es-ES", "fr-FR", "de-DE", "it-IT", "ja-JP"])

    if st.button("Start Recording"):
        speech_to_text(language)

if __name__ == "__main__":
    main()
