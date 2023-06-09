import streamlit as st
import openai
from audiorecorder import audiorecorder
from PIL import Image
import time
import random
openai.api_key = "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"

# front end elements of the web page 
html_temp = """ 
    <div style ="background-color:skyblue;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Vi-Chat</h1> 
    </div> 
    """

      # display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
st.subheader('by Clawcode team')

st.title('from speech to image')

def audio_to_file(audio):
    file_name = "audio/"+str(time.time())+str(random.randint(1000,9999))+".mp3"
    wav_file = open(file_name, "wb")
    wav_file.write(audio.tobytes())
    return file_name

def audiototext(file_name):
    audio_file= open(file_name, "rb")
    transcript = openai.Audio.translate("whisper-1", audio_file)
    # print(transcript)
    return transcript.text

def text_to_img(text):
    response = openai.Image.create(
        prompt=text,
        n=1,
        size="1024x1024",
    )
    return response['data'][0]['url']


st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    st.write("Saving Audio ...")
    file = audio_to_file(audio)
    st.write("Processing Audio ...")
    text = audiototext(file)
    st.write("Generating Response ...")
    image_link = text_to_img(text)
    st.image(image_link, caption=text)

