dir=$PWD
parentdir="$(dirname "$dir")"
parentdir="$(dirname "$parentdir")"

### Values to change, if any ###
custom_model_name='final_model.pt'
finetuned_model_path=$parentdir'/checkpoints/finetuning/checkpoint_best.pt'
pretrained_model_path=$parentdir'/checkpoints/pretraining/CLSRIL-23.pt'
custom_model_path=$parentdir'/checkpoints/custom_model/'
dictionary=$parentdir'/data/finetuning/dict.ltr.txt'

### Values to change end ###
echo "Generating Custom Model"

mkdir -p ${custom_model_path}
python ../../utils/inference/generate_custom_model.py -f ${finetuned_model_path} -p ${pretrained_model_path} -d ${dictionary} -o ${custom_model_path}${custom_model_name}

echo "\nModel saved at :"${custom_model_path}"\n"

echo "Copying finetuning dictionary from: "${dictionary} " to: "${custom_model_path}
cp ${dictionary} ${custom_model_path}
echo "Completed"

