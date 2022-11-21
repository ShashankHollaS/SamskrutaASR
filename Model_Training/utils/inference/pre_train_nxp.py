import torch
import os
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

model_path = "facebook/wav2vec2-large-960h-lv60-self"

processor = Wav2Vec2Processor.from_pretrained(model_path)
model = Wav2Vec2ForCTC.from_pretrained(model_path)

dummy_input = torch.rand([1,3600])
input_names = ['input']
output_names = ['output']

torch.onnx.export(model, dummy_input, 'wav2vec2.onnx', verbose=True, input_names=input_names, output_names = output_names)
