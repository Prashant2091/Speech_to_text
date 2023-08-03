import streamlit as st
import speech_recognition as sr
from googletrans import Translator
import webrtcvad

def speech_to_text(language="en"):
    r = sr.Recognizer()

    with sr.AudioFile("audio.wav") as source:
        st.write("Speak now...")
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
        with st.spinner("Recording..."):
            vad = webrtcvad.Vad()
            vad.set_mode(1)

            mic = sr.Microphone()
            with mic as source:
                audio_data = r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            with open("audio.wav", "wb") as f:
                f.write(audio.get_wav_data())

        speech_to_text(language_code)

if __name__ == "__main__":
    main()
