# import torch
# model = torch.load('/home/holla/vakyansh-wav2vec2-experimentation/checkpoints/custom_model/final_model.pt')
# model.eval()
# wav_in = torch.randn(100)
# torch.onnx.export(model, wav_in, 'onnx_model.onnx', export_params=True, verbose=True, do_constant_folding=True, input_names = ['input'], output_names = ['output'])

import onnx
import onnxruntime
import torch
from scipy.io import wavfile
import numpy as np

import soundfile as sf
# from scipy.io import wavfile
import scipy.signal as sps
import os
# from pythainlp.util import normalize
#model = torch.load('wav2vec2.onnx')
# input = wavfile.read('speech_orig.wav')
# wav_in = input[1].astype(np.float)
# session = onnxruntime.InferenceSession('wav2vec2.onnx', None)
# input_name = session.get_inputs()[0].name
# output_name = session.get_outputs()[0].name

# result = session.run([output_name], {input_name: wav_in})
# prediction=int(np.argmax(np.array(result).squeeze(), axis-0))
# print(prediction)
input_size = 3600
new_rate = 16000
AUDIO_MAXLEN = input_size

ort_session = onnxruntime.InferenceSession('wav2vec2.onnx')


def _normalize(x): #
  """You must call this before padding.
  Code from https://github.com/vasudevgupta7/gsoc-wav2vec2/blob/main/src/wav2vec2/processor.py#L101
  Fork TF to numpy
  """
  # -> (1, seqlen)
  mean = np.mean(x, axis=-1, keepdims=True)
  var = np.var(x, axis=-1, keepdims=True)
  return np.squeeze((x - mean) / np.sqrt(var + 1e-5))


def remove_adjacent(item): # code from https://stackoverflow.com/a/3460423
  nums = list(item)
  a = nums[:1]
  for item in nums[1:]:
    if item != a[-1]:
      a.append(item)
  return ''.join(a)

def asr(path):
    """
    Code from https://github.com/vasudevgupta7/gsoc-wav2vec2/blob/main/notebooks/wav2vec2_onnx.ipynb
    Fork TF to numpy
    """
    sampling_rate, data = wavfile.read(path)
    samples = round(len(data) * float(new_rate) / sampling_rate)
    new_data = sps.resample(data, samples)
    speech = np.array(new_data, dtype=np.float32)
    speech = _normalize(speech)[None]
    padding = np.zeros((speech.shape[0], -(AUDIO_MAXLEN - speech.shape[1])))
    speech = np.concatenate([speech, padding], axis=-1).astype(np.float32)
    ort_inputs = {"modelInput": speech}
    ort_outs = ort_session.run(None, ort_inputs)
    prediction = np.argmax(ort_outs, axis=-1)
    # Text post processing
    _t1 = ''.join([res[i] for i in list(prediction[0][0])])
    return normalize(''.join([remove_adjacent(j) for j in _t1.split("[PAD]")]))


asr('speech_orig.wav')