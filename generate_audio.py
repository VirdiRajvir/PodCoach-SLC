# from dotenv import load_dotenv
# from elevenlabs.client import ElevenLabs
# from elevenlabs import play
# import os

# load_dotenv()

# elevenlabs = ElevenLabs(
#   api_key=os.getenv("ELEVENLABS_API_KEY"),
# )


# def generate_audio_file(text, output_path='static/audio/generated_audio.mp3',
#                         voice_id="JBFqnCBsd6RMkjVDRZzb",
#                         model_id="eleven_multilingual_v2",
#                         output_format="mp3_44100_128"):
#     """
#     Generates speech from text and saves it as an MP3 file.

#     Args:
#         text (str): Text to convert to speech.
#         output_path (str): Path where the MP3 file will be saved.
#         voice_id (str): ElevenLabs voice ID.
#         model_id (str): ElevenLabs model ID.
#         output_format (str): Audio format.

#     Returns:
#         str: Path to the saved MP3 file.
#     """

#     audio_stream = elevenlabs.text_to_speech.convert(
#         text=text,
#         voice_id=voice_id,
#         model_id=model_id,
#         output_format=output_format
#     )

#     # Write audio stream to file
#     with open(output_path, 'wb') as f:
#         for chunk in audio_stream:
#             f.write(chunk)

#     return output_path

from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os


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