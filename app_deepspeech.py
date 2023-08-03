import streamlit as st
import speech_recognition as sr
from google.cloud import translate_v2 as translate
from st_voice_recorder import voice_recorder

def speech_to_text(language="en"):
    r = sr.Recognizer()

    st.write("Please record your speech using the voice recorder below.")

    # Get audio recording from the voice recorder component
    audio_data = voice_recorder()

    try:
        # Perform speech recognition
        audio_text = sr.AudioData(audio_data)
        text = r.recognize_google(audio_text, language=language)
        st.write("Transcription:")
        st.write(text)

        # Language translation
        translate_client = translate.Client()
        translated_text = translate_client.translate(text, target_language="en")
        st.write("Translation (English):")
        st.write(translated_text["translatedText"])

    except sr.UnknownValueError:
        st.error("Sorry, could not understand audio.")
    except sr.RequestError as e:
        st.error(f"Error fetching results from Google Speech Recognition service: {e}")
    except Exception as e:
        st.error(f"Error: {e}")

def main():
    st.title("Speech-to-Text Converter")
    st.write("Select the language and record your speech using the voice recorder below.")

    language_options = {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Italian": "it",
        "Japanese": "ja",
    }

    language = st.selectbox("Select Language", list(language_options.keys()))
    language_code = language_options[language]

    speech_to_text(language_code)

if __name__ == "__main__":
    main()
