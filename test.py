from flair.data import Sentence
from flair.models import SequenceTagger

from tqdm import tqdm
import json

from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import TransformerWordEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer

columns = {1: 'text', 4: 'ner'}
corpus: Corpus = ColumnCorpus('/content/Dataset_tr_ts_valid/mt5_valid', columns,
                              train_file='train.txt',
                              dev_file='test.txt',
                              test_file='valid.txt'
                              )

# load the model you trained
model_mean = SequenceTagger.load('/content/mt5-large/best_ model_large.pt')

result_mean = model_mean.evaluate(corpus.test, gold_label_type='ner',mini_batch_size=4, out_path=f"/content/mt5-large/pred_valid.txt")
print(result_mean)
