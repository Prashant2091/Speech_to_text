import streamlit as st
import speech_recognition as sr
from googletrans import Translator
import sounddevice as sd
import numpy as np

def record_audio():
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording

    st.write("Speak now...")

    # Record audio
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    # Save audio as a WAV file
    file_path = "audio.wav"
    wav_data = np.int16(audio * 32767)  # Convert audio to 16-bit integers
    with open(file_path, "wb") as f:
        f.write(wav_data.tobytes())

    st.write("Recording saved.")

    return file_path

def speech_to_text(language="en"):
    r = sr.Recognizer()

    file_path = record_audio()

    with sr.AudioFile(file_path) as source:
        audio = r.record(source)

    try:
        st.write("Transcription:")
        text = r.recognize_google(audio, language=language)
        st.write(text)

        # Language translation
        translator = Translator()
        translated_text = translator.translate(text, src=language, dest="en")
        st.write("Translation (English):")
        st.write(translated_text.text)

    except sr.UnknownValueError:
        st.error("Sorry, could not understand audio.")
    except sr.RequestError as e:
        st.error(f"Error fetching results from Google Speech Recognition service: {e}")
    except Exception as e:
        st.error(f"Error: {e}")

def main():
    st.title("Speech-to-Text Converter")
    st.write("Select the language and start speaking.")

    language_options = {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Italian": "it",
        "Japanese": "ja",
    }

    language = st.selectbox("Select Language", list(language_options.keys()))

    if st.button("Start Recording"):
        language_code = language_options[language]
        speech_to_text(language_code)

if __name__ == "__main__":
    main()
