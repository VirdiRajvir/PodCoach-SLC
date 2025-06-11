from gtts import gTTS

def generate_audio(text, username, goal, output_path='static/audio/generated_audio.mp3'):
    """
    Generates speech from text and saves it as an MP3 file.

    Args:
        text (str): Text to convert to speech.
        output_path (str): Path where the MP3 file will be saved.

    Returns:
        str: Path to the saved MP3 file.
    """
    
    # Create a gTTS object
    tts = gTTS(text=text, lang='en', slow=False)
    
    # Save the audio file
    tts.save(output_path)
    
    
    return output_path