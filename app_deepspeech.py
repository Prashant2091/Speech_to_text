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

    language = st.selectbox("Select Language", ["en-US", "es-ES", "fr-FR", "de-DE", "it-IT", "ja-JP"])

    if st.button("Start Recording"):
        speech_to_text(language)

if __name__ == "__main__":
    main()
