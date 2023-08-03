import streamlit as st
import speech_recognition as sr

def speech_to_text(language="en"):
    r = sr.Recognizer()

    st.write("Please record your speech using the voice recorder below.")

    # Get audio recording from the voice recorder component
    audio_data = st.record("record_button")

    try:
        # Perform speech recognition
        text = r.recognize_google(audio_data, language=language)
        st.write("Transcription:")
        st.write(text)

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

    # Add a record button to start recording audio
    record_button = st.button("Start Recording")

    if record_button:
        speech_to_text(language_code)

if __name__ == "__main__":
    main()
