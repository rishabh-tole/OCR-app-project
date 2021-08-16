import speech_recognition as sr 
import os, shutil
from pydub import AudioSegment
from pydub.silence import split_on_silence


import subprocess

class AudioToText():

    def __init__(self):
        self.r = sr.Recognizer()


# create a speech recognition object

# a function that splits the audio file into chunks
# and applies speech recognition


    def get_file_name(self):
        
        subprocess.call(['ffmpeg', '-i', 'volcanoe.mp3','volcanoe.wav'])

    def get_large_audio_transcription(self,path):
        """
        Splitting the large audio file into chunks
        and apply speech recognition on each of these chunks
        """
        # open the audio file using pydub
        sound = AudioSegment.from_wav(path)  
        # split audio sound where silence is 700 miliseconds or more and get chunks
        chunks = split_on_silence(sound,
            # experiment with this value for your target audio file
            min_silence_len = 700,
            # adjust this per requirement
            silence_thresh = sound.dBFS-14,
            # keep the silence for 1 second, adjustable as well
            keep_silence=500,
        )
        folder_name = "audio-chunks"
        # create a directory to store the audio chunks
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        whole_text = ""
        # process each chunk 
        for i, audio_chunk in enumerate(chunks, start=1):
            # export audio chunk and save it in
            # the `folder_name` directory.
            chunk_filename = os.path.join(folder_name, "chunk{}.wav".format(i))
            audio_chunk.export(chunk_filename, format="wav")
            # recognize the chunk
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = self.r.record(source)
                # try converting it to text
                try:
                    text = self.r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    pass
                    #print("Error:", str(e))
                else:
                    text = "{}. ".format(text.capitalize)
                    #print(chunk_filename, ":", text)
                    whole_text += text
        # return the text for all chunks detected
        shutil.rmtree(folder_name)
        return whole_text
