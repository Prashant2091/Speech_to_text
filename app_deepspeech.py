import streamlit as st
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

    language = st.selectbox("Select Language", ["English", "Spanish"])  # Add more options as needed

    if st.button("Convert"):
        text = speech_to_text(language)
        st.write("Text:", text)

if __name__ == "__main__":
    main()
