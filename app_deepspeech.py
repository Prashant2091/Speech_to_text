import streamlit as st
import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder

def speech_to_text(language="en"):
    r = sr.Recognizer()

    st.write("Click the 'Start Recording' button and speak.")

    if st.button("Start Recording"):
        audio_data = record_audio()
        if audio_data:
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

def record_audio():
    audio_data = None
    with st.spinner("Recording..."):
        try:
            audio_bytes = audio_recorder()
            if audio_bytes:
                # st.audio(audio_bytes, format="audio/wav")
                audio_data = st.audio(audio_bytes, format="audio/wav")
        except Exception as e:
            st.error(f"Error during audio recording: {e}")

    return audio_data

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

    speech_to_text(language_options[language])

if __name__ == "__main__":
    main()
