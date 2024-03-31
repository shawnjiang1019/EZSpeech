from typing import Sequence
import os
import google.cloud.texttospeech as tts

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "API_KEY.json"

def text_to_wav(lan_code: str, text: str, pitch: float, speed: float):
    language_code = lan_code
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code
    )
    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.LINEAR16,
        pitch = pitch, # [-20, 20]
        speaking_rate = speed #[0.25, 4]
        )

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )

    filename = "output.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')
        

# Create an audio file output
# Parameter lists:
    # 1. language_code
    # 2. Text 
    # 3. pitch [-20, 20]
    # 4. speed [0.25, 4]
text_to_wav('en', "Hi how are you?", 0, 0.8)
