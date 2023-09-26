import streamlit as st
import speech_recognition as sr

def speech_to_text(language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language=language)
        st.success("Text: {}".format(text))
    except sr.UnknownValueError:
        st.error("Could not understand audio")
    except sr.RequestError as e:
        st.error("Could not request results; {}".format(e))

def main():
    st.title("Speech to Text Converter")
    language = st.selectbox("Select Language", ["English", "Spanish", "German", "French", "Italian", "Dutch", 
                                                "Portuguese", "Russian", "Chinese", "Japanese", "Korean", 
                                                "Arabic", "Hindi", "Swedish", "Turkish"])
    language_code = {"English": "en", "Spanish": "es", "German": "de", "French": "fr", "Italian": "it",
                     "Dutch": "nl", "Portuguese": "pt", "Russian": "ru", "Chinese": "zh-CN", "Japanese": "ja",
                     "Korean": "ko", "Arabic": "ar", "Hindi": "hi", "Swedish": "sv", "Turkish": "tr"}
    if st.button("Start Recording"):
        speech_to_text(language_code[language])

if __name__ == "__main__":
    main()
