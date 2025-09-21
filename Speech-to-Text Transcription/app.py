import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

def transcribe_audio_file(audio_file):
    """Transcribe speech from an audio file"""
    try:
        with sr.AudioFile(audio_file) as source:
            print("Loading audio file...")
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="en-IN")
        print("\n[File Transcription]:")
        print(text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Error: Could not request results from the service.")
    except FileNotFoundError:
        print("Audio file not found.")

def transcribe_from_mic():
    """Transcribe live speech from the microphone continuously"""
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("🎤 Start speaking. Press Ctrl+C to stop.")
            
            while True:
                print("Listening...")
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)
                try:
                    text = recognizer.recognize_google(audio, language="en-IN")
                    print("[You said]:", text)
                except sr.UnknownValueError:
                    print("Could not understand audio.")
                except sr.RequestError:
                    print("Error requesting results from the service.")

    except KeyboardInterrupt:
        print("\nStopped listening.")
    except Exception as e:
        print(f"Microphone Error: {e}")

if __name__ == "__main__":
    print("Choose Input Method:")
    print("1. Upload Audio File")
    print("2. Live Microphone Input")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        file_path = input("Enter path to audio file (e.g., sample.wav): ")
        transcribe_audio_file(file_path)
    elif choice == "2":
        transcribe_from_mic()
    else:
        print("Invalid choice. Exiting...")