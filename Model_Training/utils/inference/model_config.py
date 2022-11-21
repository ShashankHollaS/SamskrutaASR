import torch
from single_file_inference import Wav2VecCtc
from torchsummary import summary
model_path = '/home/holla/vakyansh-wav2vec2-experimentation/checkpoints/custom_model/final_model.pt'
model = torch.load(model_path)
#summary(model, input_size-(1,))
print(model)