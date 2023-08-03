import streamlit as st
import speech_recognition as sr

def speech_to_text(language="en"):
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
        speech_to_text(language_code)

if __name__ == "__main__":
    main()
