# Master thesis Named Entity Recognition in Speech to Text Transcripts
Master thesis on Proper Capitalization in Speech to Text Transcripts using NER

This repository contain code and results from the conducted experiments.

## Abstract
Traditionally, named entity recognition (NER) research use properly capitalized data for training in testing, however, these results give little insight to how these models may perform in scenarios where proper capitalization is not in place. In this thesis, we explore the capabilities of five fine-tuning BERT based models for NER in all lowercase text. Furthermore, the aim is to measure the performance for classify named entity types correctly, as well as just simply detecting that a named entity is present, so a capitalization error may be corrected. The performance will be assessed using all lowercase data from the NorNE dataset, and the Norwegian Parliamentary Speech Corpus.



|     Model     |   Precision  |      Recall     | F1-Score |
|:-------------:|:------------:|:---------------:|:--------:|
|    SpaCy*      |     52.42    |       54.24     |  83.36   |
|    NCRF++      |     35.69    |       33.07     |  75.42   |
|     mBERT      | 81.88 (±0.67)| 80.27 (±0.87)   | 95.17 (±0.52) |
|    NorBERT     | 81.71 (±1.74)| 79.00 (±1.74)   | 96.19 (±0.49) |
|    NorBERT2    | 80.77 (±0.81)| 77.59 (±0.73)   | 96.52 (±0.19) |
|    NB-BERT     | **84.44** (±0.55)| **82.30** (±0.84)| **96.62** (±0.22)|
|   Ner-Scandi   | 83.72 (±1.00)| 81.08 (±1.33)   | 96.26 (±0.37) |

Table: The annotated NPSC sample dataset results for all models. BERT models use the average F1 across all seeds for a given model. No Boundary denotes NER without named entity token span taken into account. Strict Match denotes NER with named entity token span taken into the evaluation. Binary Classification denotes the task where only the detection if an entity is present, without specific type associated. *3 sentences were dropped from SpaCy pipeline.
