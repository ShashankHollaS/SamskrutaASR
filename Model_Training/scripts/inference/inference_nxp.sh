dir=$PWD
parentdir="$(dirname "$dir")"
parentdir="$(dirname "$parentdir")"

### Values to change, if any ###
custom_model_path=$parentdir'/checkpoints/custom_model/final_model.pt'
#custom_model_path='/home/holla/Downloads/sanskrit_infer.pt'
dictionary=$parentdir'/data/finetuning/dict.ltr.txt'
wav_file_path='/home/holla/Downloads/new_81.wav' # path to single wav file
decoder="kenlm" # viterbi or kenlm
cuda=False
half=False

#If kenlm
lm_name='Samskruta_1'
lm_model_path=${parentdir}'/lm/'${lm_name}'/lm.binary'
lexicon_lst_path=${parentdir}'/lm/'${lm_name}'/lexicon.lst'

### Values to change end ###

if [ "$decoder" = "viterbi" ]
then
	python ../../utils/inference/inference_nxp.py -m ${custom_model_path} -d ${dictionary} -w ${wav_file_path} -c ${cuda} -D ${decoder} -H ${half}
else
	python ../../utils/inference/inference_nxp.py -m ${custom_model_path} -d ${dictionary} -w ${wav_file_path} -c ${cuda} -D ${decoder} -l ${lexicon_lst_path} -L ${lm_model_path} -H ${half} 
fi
