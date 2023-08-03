import streamlit as st
import tempfile
import os
import numpy as np
import speech_recognition as sr
import pyaudio

def audio_callback(in_data, frame_count, time_info, status):
    global temp_buffer
    temp_buffer.append(in_data)
    if len(temp_buffer) > num_segments:
        save_and_transcribe_audio()
    return (None, pyaudio.paContinue)

def save_and_transcribe_audio():
    global temp_buffer
    frames = np.concatenate(temp_buffer)
    temp_buffer = []
    
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
        temp_wav_file = fp.name
        fp.write(frames.tobytes())
    
    speech_to_text(temp_wav_file)

def speech_to_text(wav_file):
    r = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio = r.record(source)
    
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

def main():
    global temp_buffer, num_segments, sample_rate, language
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
        temp_buffer = []
        num_segments = 5  # Number of segments to split the audio for VAD
        sample_rate = 44100  # Adjust this based on your microphone's sample rate
        
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, stream_callback=audio_callback)
        
        st.write("Speak now... (Press the 'Stop Recording' button to finish)")
        st.button("Stop Recording")
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()
