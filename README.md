# Astro-mT5
This repository contains code and the paper for [ Astro-mT5: Entity Extraction from Astrophysics Literature using mT5 Language Model ] accepted at AACL-IJCNLP Workshop '2022.

## Abstract <a name="task"></a>
Scientific research requires reading and extracting relevant information from existing scientific literature in an effective way. To gain insights over a collection of such scientific documents, extraction of entities and recognizing their types is considered to be one of the important tasks. Numerous studies have been conducted in this area of research. In our study, we introduce a framework for entity recognition and identification of NASA astrophysics dataset, which was published as a part of the DEAL SharedTask. We use a pre-trained multilingual model, based on a natural language processing framework for the given sequence labeling tasks. Experiments show that our model, Astro-mT5, outperforms the existing baseline in astrophysics related information extraction. Our paper is available at [work](https://drive.google.com/file/d/1Mxc6pu47H5qHvGm2uzzY3-70LX37AccP/view?usp=sharing).

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
