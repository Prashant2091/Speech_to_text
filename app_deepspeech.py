import streamlit as st
import speech_recognition as sr
import soundfile as sf
import tempfile
import os

def save_audio(audio_data, filename):
    with open(filename, "wb") as f:
        f.write(audio_data.get_wav_data())

def speech_to_text(language="en"):
    r = sr.Recognizer()

    st.write("Please record your speech using the voice recorder below.")

    # Add a record button to start recording audio
    record_button = st.button("Start Recording")

    if record_button:
        # Create a temporary file to store the recorded audio
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_filename = temp_file.name

        # Record audio
        with st.audio(recording=True, format="audio/wav") as audio_data:
            st.write("Recording...")

        # Save recorded audio to a temporary file
        save_audio(audio_data, temp_filename)

        # Read the audio file and perform speech recognition
        with sr.AudioFile(temp_filename) as audio:
            try:
                text = r.recognize_google(audio, language=language)
                st.write("Transcription:")
                st.write(text)

            except sr.UnknownValueError:
                st.error("Sorry, could not understand audio.")
            except sr.RequestError as e:
                st.error(f"Error fetching results from Google Speech Recognition service: {e}")
            except Exception as e:
                st.error(f"Error: {e}")

        # Remove the temporary audio file
        os.remove(temp_filename)

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
