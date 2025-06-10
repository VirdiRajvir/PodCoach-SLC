import elevenlabs

def generate_audio(text, voice = "Bella"):
    audio = elevenlabs.generate(
        text=text,
        voice=voice
    )
    elevenlabs.save(audio, 'static/audio/coaching_script.mp3')
    return 'coaching_script.mp3'