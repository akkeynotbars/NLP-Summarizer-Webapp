from speech_to_text import speech_to_text

def run_test():
    """
    Validation script to test the Speech-to-Text functionality locally.
    """
    # Provide a short audio file (e.g., 'test_audio.wav') in this folder
    filename = "test_audio.wav" 
    
    try:
        with open(filename, "rb") as f:
            audio_data = f.read()
            print(f"Processing audio: {filename}...")
            
            # Execute the function
            transcription = speech_to_text(audio_data)
            
            print("-" * 30)
            print(f"Transcription Result:\n{transcription}")
            print("-" * 30)
            
    except FileNotFoundError:
        print(f"Error: Please place an audio file named '{filename}' in this folder to run the test.")
    except Exception as e:
        print(f"An error occurred during testing: {e}")

if __name__ == "__main__":
    run_test()