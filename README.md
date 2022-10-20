# Astro-mT5
This repository contains code for [ Astro-mT5: Entity Extraction from Astrophysics Literature using mT5 Language Model ] at DEAL WIESP 2022.

## Setup
Install Package Dependencies

`git clone https://github.com/flairNLP/flair.git`  <br>
`cd flair` <br>
`git checkout add-t5-encoder-support`  <br>
`pip3 install -e .` <br>
For running the experiment `run_ner.py` and `test.py` have to be kept inside the flair directory.

## Training
The main training procedure is: <br>
`python3 run_ner.py --dataset_name NER_MASAKHANE \ `  <br>
  `--model_name_or_path google/mt5-large\`  <br>
  `--layers -1\` <br>
  `--subtoken_pooling first_last\`  <br>
  `--hidden_size 256\`  <br>
  `--batch_size 4\`  <br>
  `--learning_rate 5e-05\`  <br>
  `--num_epochs 100\`  <br>
  `--use_crf True\`  <br>
  `--output_dir /content/mt5-large`

## Tesing
After training, you can find the best checkpoint on the dev set according to the evaluation results.
For this run <br> `python3 test.py`
