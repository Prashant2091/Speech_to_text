import streamlit as st
import speech_recognition as sr

# Set page title and format
st.set_page_config(page_title="Speech to Text Converter", layout="wide")

# Define function for speech recognition
def convert_speech_to_text(audio_file, language):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language=language)
        return text

# Main app function
def main():
    # Set app title and description
    st.title("Speech to Text Converter")
    st.write("Upload an audio file and choose the language to convert speech to text!")

    # Audio file upload
    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

    if uploaded_file:
        st.write("File uploaded successfully!")

        # Language selection
        language = st.selectbox("Select the language", ["English", "Spanish", "French"])
        language_code = "en-US"  # Default to English (United States)

        # Map language to language code
        if language == "Spanish":
            language_code = "es-ES"
        elif language == "French":
            language_code = "fr-FR"

        # Convert speech to text
        text = convert_speech_to_text(uploaded_file, language=language_code)

        # Display converted text
        st.subheader("Converted Text")
        st.write(text)

    # Add some space
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    # Footer
    st.markdown("---")
    st.write("Created with ❤️ by Your Name")

# Run the app
if __name__ == "__main__":
    main()
