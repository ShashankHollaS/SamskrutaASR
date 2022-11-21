from flask import Flask, render_template, request, redirect
import os
import random
import single_file_inference as inf

from single_file_inference import Wav2VecCtc

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
		
	return render_template('index.html', transcript=transcript)

if __name__ == '__main__':
	app.run(debug=True, threaded=False)
