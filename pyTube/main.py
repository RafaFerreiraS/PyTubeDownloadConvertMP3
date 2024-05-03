from flask import Flask, render_template, request, redirect
from pytube import YouTube
from moviepy.editor import *
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    diretorio = request.form['dir'].replace('/', '//')
    video = YouTube(url)
    video.streams.get_audio_only().download(diretorio)
    MP4ToMP3(diretorio +'\\'+ video.title + '.mp4', diretorio +'\\'+ video.title + '.mp3')
    os.remove(diretorio +'\\'+ video.title + '.mp4')
    return redirect('/')


def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()


if __name__ == '__main__':
    app.run(debug=True, port=8082)
