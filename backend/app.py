
import queue
import re
import sys
from flask import Flask, render_template, request, flash, redirect, url_for, session
from google.cloud import speech
from transcribe import *
from translate import *

import pyaudio

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate') 
def translate():
    return render_template('translate.html')

@app.route('/transcribe/<language>', methods=['GET'])
def transcribe_audio(language):
   
    
    language_code = language  
    
    client = speech.SpeechClient.from_service_account_file('C:/Users/shawn/Documents/EZSpeech/easyspeech-418815-aa07c590833f.json')  # Update with your service account path
    
    # Configure speaker diarization
    diarization_config = speech.SpeakerDiarizationConfig(
        enable_speaker_diarization=True,
        min_speaker_count=2,
        max_speaker_count=2
    )
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code='en-US',  # Specify multiple languages here
        diarization_config=diarization_config,
        alternative_language_codes=['zh-CN', 'fr-FR']  # Specify alternative languages here
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        interim_results=True
    )

    with MicrophoneStream(RATE, CHUNK) as stream:  
        audio_generator = stream.generator()
        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        responses = client.streaming_recognize(streaming_config, requests)
        
        listen_print_loop(responses, 'text')

    return "Transcription started for language: " + language_code


@app.route('/translate/<language>', methods=['GET'])
def translate_file(language):
    # get the input and target files
    target = open('text2.txt', 'a')
    input = open('text.txt', 'r')
    # get the entire text file as a list then iterate and translate each string in the list
    lines=[]
    for line in input:
        lines.append(line.strip())
    translated = ''
    for line in lines:
        translated = translate_text(language, line)
        #write the text into this file
        
        target.write(translated['translatedText'] + '\n')
    
    return "Translated"









if __name__ == '__main__':
    app.run()