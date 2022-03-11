import os
from flask import Flask,flash,render_template,jsonify,redirect,request
import random
import single_file_inference as inf
import subprocess
import wave
import base64
import librosa
import soundfile as sf
import requests

from single_file_inference import Wav2VecCtc
#UPLOAD_FOLDER = 'uploads/audios/'
#ALLOWED_EXTENSIONS = {'wav'}

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#def predict(file):
#    return file.filename
transcript = ''
@app.route("/", methods=['GET','POST'])
def index():
    #global transcript
    #if transcript == '':
        #transcript='nodu'
    #print(transcript)
    return render_template('index1.html', transcript=transcript)

@app.route("/result/", methods=['POST'])
def final():
    if 'file' not in request.files:
            print("illa")
            flash('No file part')
            return redirect(request.url)
    file = request.files['file']
    if file :
        file.save('check1.ogg')
        model_path = 'final_model.pt'
        dict_path = 'dict.ltr.txt'

        exit_code = subprocess.call('./process.sh') 
        wav_path = 'audio.wav'
        cuda = False
        decoder = 'kenlm'
        half = False
        lexicon_path = 'lexicon.lst'
        lm_path = 'lm.binary'
        transcript = inf.parse_transcription(model_path, dict_path, wav_path, cuda, decoder, lexicon_path, lm_path, half)
        os.remove('audio.wav')
        os.remove('check1.ogg')
        os.remove('check1.wav')
        #print('aytu')
        #return jsonify(transcript)
        #requests.put('http://127.0.0.1:5000/')
        #transcript = 'check'
        #print(type(transcript))
        print("Transcript:", transcript)
        return transcript
    

if __name__=='__main__':
    #app.run(debug=True,port=8080)
    app.run(host ='0.0.0.0', debug=True, threaded=True)

#form = request.form
        #data_prev = form['file']
        #print(data_prev)
        #data = base64.b64decode(data_prev)
        #print(data)
        #print(type(file))
        #print(type('/home/holla/single.wav'))
        #with wave.open('audio.wav', 'wb') as audio:
        #file.save(audio)
        #file.filename = request.form['fname']
#if data :
            #print(type(data))
            #data = bytearray("".join(["{:08b}".format(x) for x in data]), 'utf8')
            #x,_ = librosa.load(file, sr=16000)
            #sf.write('tmp.wav', x, 16000)
            #obj1 = wave.open('tmp.wav', 'r')
            #data = obj1.readnframes(obj1.getnframes())
            #obj = wave.open('audio.wav','wb')
            #obj.setnchannels(1)
            #obj.setsampwidth(2)
            #obj.setframerate(16000)
            #obj.writeframes(file.read())'''
            #obj.write(data)
            #wav_file =  open('audio.wav', 'wb')
            #w
            #obj.save()
            #obj.close()
            #obj1.close()
            #wav_file = open('audio.wav','wb')
            #wav_file.write(data)
            #file_name = str(random.randint(0,10000)) + '.wav'
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
#wav_path = 'home/holla/Downloads/file1.wav' #+ file_name
#wav_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

#os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            #print(transcript)
            #output = predict(file)
