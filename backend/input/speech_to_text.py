import whisper
import tempfile
import os

# Load the 'base' model for a good balance between speed and accuracy
model = whisper.load_model("base")

def speech_to_text(audio_bytes: bytes) -> str:
    """
    Converts raw audio data (bytes) into a text string using OpenAI Whisper.
    
    Args:
        audio_bytes (bytes): The raw binary data of the audio file.
        
    Returns:
        str: The transcribed text.
    """
    # Whisper requires a physical file path, so we create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_path = temp_audio.name

    try:
        # Transcribe the audio file to text
        result = model.transcribe(temp_path)
        return result["text"].strip()
    finally:
        # Clean up the temporary file to save storage space
        if os.path.exists(temp_path):
            os.remove(temp_path)