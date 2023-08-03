import streamlit as st
import tempfile
import os
import sounddevice as sd
import numpy as np
import webrtcvad
import speech_recognition as sr

def audio_callback(indata, frames, time, status):
    temp_buffer.append(indata.copy())
    if len(temp_buffer) > num_segments:
        vad_detection()

def vad_detection():
    global temp_buffer
    frames = np.concatenate(temp_buffer)
    temp_buffer = []
    
    vad = webrtcvad.Vad()
    vad.set_mode(2)
    
    frames_bytes = frames.tobytes()
    segments = vad_collector(vad, frames_bytes, sample_rate)
    
    for i, segment in enumerate(segments):
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
            temp_wav_file = fp.name
            fp.write(segment)
        speech_to_text(temp_wav_file)

def vad_collector(vad, frames_bytes, sample_rate):
    frames = frames_bytes
    frames_len = len(frames)
    frame_duration_ms = int(1000 * 10 / sample_rate)
    frame_duration = int(sample_rate * frame_duration_ms / 1000)
    in_speech = False
    offset = 0
    segments = []
    while offset < frames_len:
        frame = frames[offset:offset + frame_duration]
        if vad.is_speech(frame, sample_rate):
            segments.append(frame)
            in_speech = True
        elif in_speech:
            segments.append(frame)
            in_speech = False
        offset += frame_duration
    return [np.array(seg, dtype=np.int16) for seg in segments]

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
        with sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate):
            st.write("Speak now... (Press the 'Stop Recording' button to finish)")
            st.button("Stop Recording")

if __name__ == "__main__":
    main()
