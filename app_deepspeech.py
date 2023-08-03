import streamlit as st
import speech_recognition as sr

def speech_to_text(language="en-US"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = r.listen(source)

    try:
        st.write("Transcription:")
        text = r.recognize_google(audio, language=language)
        st.write(text)
    except sr.UnknownValueError:
        st.error("Sorry, could not understand audio.")
    except sr.RequestError as e:
        st.error("Error fetching results from Google Speech Recognition service; {0}".format(e))

def main():
    st.title("Speech-to-Text Converter")
    st.write("Select the language and start speaking.")

    language_options = {
        "English (US)": "en-US",
        "Spanish": "es-ES",
        "French": "fr-FR",
        "German": "de-DE",
        "Italian": "it-IT",
        "Japanese": "ja-JP",
    }

    language = st.selectbox("Select Language", list(language_options.keys()))

    if st.button("Start Recording"):
        language_code = language_options[language]
        speech_to_text(language_code)

if __name__ == "__main__":
    main()
