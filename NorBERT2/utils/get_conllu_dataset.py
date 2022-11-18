# Heavily insipired from:
# https://github.com/ltgoslo/NorBERT/blob/main/benchmarking/experiments/dataset.py
from torch.utils.data import Dataset
import torch

class CoNLLDataset(Dataset):
    def __init__(self, x_tokens, y_labels, ner_vocab=None):
        self.tokens = [[x for x in entry] for entry in x_tokens]
        self.ner_labels = [[y for y in entry] for entry in y_labels]

        # hard coded ner_vocab to avoid random shuffled instanciation of ordering of ner_vocab
        self.ner_vocab = ner_vocab
        self.ner_indexer = {i: n for n, i in enumerate(self.ner_vocab)}
    
    def __getitem__(self, index):
        tokens = self.tokens[index]
        ner_labels = self.ner_labels[index]

        x = tokens
        y = torch.LongTensor([self.ner_indexer[i] if i in self.ner_vocab
                              else self.ner_indexer['@UNK'] for i in ner_labels])
        return x, y

    def __len__(self):
        return len(self.tokens)

