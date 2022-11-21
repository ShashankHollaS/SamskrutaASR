import torch
import soundfile as sf

def get_feature(filepath):
    def postprocess(feats, sample_rate):
        if feats.dim == 2:
            feats = feats.mean(-1)

        assert feats.dim() == 1, feats.dim()

        with torch.no_grad():
            feats = F.layer_norm(feats, feats.shape)
        return feats

    wav, sample_rate = sf.read(filepath)
    feats = torch.from_numpy(wav).float()
    feats = postprocess(feats, sample_rate)
    return feats

model_path = '/home/holla/vakyansh-wav2vec2-experimentation/checkpoints/custom_model/final_model.pt'
wav_path = '/home/holla/Downloads/81.wav'
model = torch.load(model_path)
model.eval()
feature = get_feature(wav_path)
model_out = model(feature)

torch.onnx.export(model, feature, 'onnx_model.onnx', export_params=True, opset_version=10)
