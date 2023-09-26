import streamlit as st
import pyaudio
import speech_recognition as sr

def speech_to_text(language):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Speak something...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Could not connect to the service"

def main():
    st.title("Speech to Text Converter")
    language_options = {
    "en-US": "English",
    "es-ES": "Spanish",
    "fr-FR": "French",
    "de-DE": "German",
    "it-IT": "Italian",
    "pt-BR": "Portuguese (Brazil)",
    "ja-JP": "Japanese",
    "ko-KR": "Korean",
    "ru-RU": "Russian",
    "zh-CN": "Chinese (Simplified)",
    "ar-SA": "Arabic (Saudi Arabia)",
    "nl-NL": "Dutch",
    "hi-IN": "Hindi (India)",
    "sv-SE": "Swedish",
    "tr-TR": "Turkish"
}

    language = st.selectbox("Select Language", list(language_options.keys()))
    if st.button("Convert"):
        text = speech_to_text(language)
        st.write("Text:", text)

if __name__ == "__main__":
    main()
