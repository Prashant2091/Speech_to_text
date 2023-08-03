import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment

def speech_to_text(language="en"):
    r = sr.Recognizer()

    # Record audio using Streamlit's microphone widget
    st.write("Recording...")
    audio_data = st.record("record_button")

    # Convert audio_data to a format compatible with speech_recognition
    audio_data = AudioSegment.from_file(io.BytesIO(audio_data.getvalue()), format="wav")

    # Recognize speech using the audio data
    try:
        st.write("Transcription:")
        text = r.recognize_google(audio_data, language=language)
        st.write(text)

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
