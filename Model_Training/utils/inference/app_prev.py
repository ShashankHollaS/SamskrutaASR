#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:21:42 2021

@author: holla
"""

'''
#app1

from flask import Flask

app = Flask(__name__)  #__name__ refers to name of the current file

@app.route("/")     #python decorator

def index():
    return "hello world"
'''

'''
#app2 - Here instead of just printing something, we are returning a html page

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index1.html")
'''

'''
#app3

from flask import Flask, render_template, request #request gives access to http request

app = Flask(__name__)

@app.route("/")

def index():
    
    return render_template("index2.html", name=request.args.get("name","world")) # world is a default name, it can be changed by changing the url in the website. For changing add /?name=holla in the url
'''

'''
#app4

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("greet1.html")

@app.route("/greet")
def greet():
    return render_template("index2.html", name=request.args.get("name","world"))
'''

'''
#app5

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("greet2.html")

@app.route('/greet', methods=["POST"])  #get is default
def greet():
    return render_template("index2.html", name=request.form.get("name","world"))
'''

'''
#app6

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('greet3.html')

@app.route('/greet', methods=['POST'])
def greet():
    return render_template('index3.html', name=request.form.get('name','world'))
'''

'''
#app7

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('greet4.html')
    if request.method == 'POST':
        return render_template('index3.html', name=request.form.get('name','world'))
'''

'''
#app8

from flask import Flask, render_template, request, redirect
import speech_recognition as sr
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    transcript = ''
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
    return render_template('index4.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
'''



#app9

from flask import Flask, render_template, request, redirect
import random
import single_file_inference as inf
from single_file_inference import Wav2VecCtc 
import os
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    transcript = ''
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_name = str(random.randint(0,10000))
            file.save(file_name)
            model_path = '/home/holla/vakyansh-wav2vec2-experimentation/checkpoints/custom_model/final_model.pt'
            dict_path = '/home/holla/vakyansh-wav2vec2-experimentation/data/finetuning/dict.ltr.txt'
            wav_path = file_name
            cuda = False
            decoder = 'kenlm'
            half = False
            lexicon_path = '/home/holla/vakyansh-wav2vec2-experimentation/lm/Samskruta_1/lexicon.lst'
            lm_path = '/home/holla/vakyansh-wav2vec2-experimentation/lm/Samskruta_1/lm.binary'
            transcript = inf.parse_transcription(model_path, dict_path, wav_path, cuda, decoder, lexicon_path, lm_path, half)
            os.remove(file_name)
    return render_template('index_prev.html', transcript=transcript)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
