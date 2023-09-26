import streamlit as st
import speech_recognition as sr

# Set page title and format
st.set_page_config(page_title="Speech to Text Converter", layout="wide")

# Define function for speech recognition
def convert_speech_to_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text

# Main app function
def main():
    # Set app title and description
    st.title("Speech to Text Converter")
    st.write("Upload an audio file and convert speech to text!")

    # Audio file upload
    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

    if uploaded_file:
        st.write("File uploaded successfully!")

        # Convert speech to text
        text = convert_speech_to_text(uploaded_file)

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
