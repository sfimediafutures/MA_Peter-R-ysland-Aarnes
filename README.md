# Master thesis Named Entity Recognition in Speech to Text Transcripts
Master thesis on Proper Capitalization in Speech to Text Transcripts using NER

This repository contain code and results from the conducted experiments.

## Abstract
Traditionally, named entity recognition (NER) research use properly capitalized data for training in testing, however, these results give little insight to how these models may perform in scenarios where proper capitalization is not in place. In this thesis, we explore the capabilities of five fine-tuning BERT based models for NER in all lowercase text. Furthermore, the aim is to measure the performance for classify named entity types correctly, as well as just simply detecting that a named entity is present, so a capitalization error may be corrected. The performance will be assessed using all lowercase data from the NorNE dataset, and the Norwegian Parliamentary Speech Corpus.


## Some results from the experimets

### NorNE results
|     Model     |   Precision  |      Recall     | F1-Score |
|:-------------:|:------------:|:---------------:|:--------:|
|    SpaCy*      |     52.42    |       54.24     |  83.36   |
|    NCRF++      |     35.69    |       33.07     |  75.42   |
|     mBERT      | 81.88 (±0.67)| 80.27 (±0.87)   | 95.17 (±0.52) |
|    NorBERT     | 81.71 (±1.74)| 79.00 (±1.74)   | 96.19 (±0.49) |
|    NorBERT2    | 80.77 (±0.81)| 77.59 (±0.73)   | 96.52 (±0.19) |
|    NB-BERT     | **84.44** (±0.55)| **82.30** (±0.84)| **96.62** (±0.22)|
|   Ner-Scandi   | 83.72 (±1.00)| 81.08 (±1.33)   | 96.26 (±0.37) |

NorNE results: The annotated NPSC sample dataset results for all models. BERT models use the average F1 across all seeds for a given model. No Boundary denotes NER without named entity token span taken into account. Strict Match denotes NER with named entity token span taken into the evaluation. Binary Classification denotes the task where only the detection if an entity is present, without specific type associated. *3 sentences were dropped from SpaCy pipeline.


### NPSC binary results

| Model     | Class | Precision             | Recall                | F1                    | Support    |
|-----------|-------|-----------------------|-----------------------|-----------------------|------------|
| Spacy*    | 0     | 99.76                 | 98.28                 | 99.02                 | 1013745    |
|           | 1     | 57.27                 | 90.77                 | 70.23                 | 25723      |
|           | Macro avg. | 78.51            | 94.52                 | 84.62                 | 1039468    |
|-----------|-------|-----------------------|-----------------------|-----------------------|------------|
| NCRF++    | 0     | 97.38                 | 99.77                 | 98.56                 | 1014791    |
|           | 1     | 85.85                 | 34.04                 | 48.75                 | 41247      |
|           | Macro avg. | 91.61            | 66.91                 | 73.66                 | 1056038    |
|-----------|-------|-----------------------|-----------------------|-----------------------|------------|
| mBERT     | 0     | 99.41 (\pm{0.06})     | 99.64 (\pm{0.03})     | 99.52 (\pm{0.02})     | 1014791    |
|           | 1     | 91.09 (\pm{0.70})     | 86.18 (\pm{1.19})     | 88.56 (\pm{0.39})     | 41247      |
|           | Macro avg. | 95.25 (\pm{0.32}) | 92.91 (\pm{0.58})     | 94.04 (\pm{0.20})     | 1039468    |
|-----------|-------|-----------------------|-----------------------|-----------------------|------------|
| NorBERT   | 0     | 99.41 (\pm{0.11})     | 99.74 (\pm{0.04})     | 99.58 (\pm{0.04})     | 1014791    |
|           | 1     | 93.69 (\pm{1.04})     | 86.64 (\pm{1.97})     | 90.00 (\pm{0.66})     | 41247      |
|           | Macro avg. | 96.55 (\pm{0.47}) | 93.19 (\pm{0.97})     | 94.79 (\pm{0.35})     | 1039468    |
|-----------|-------|-----------------------|-----------------------|-----------------------|------------|
| NorBERT2  | 0     | 99.39 (\pm{0.05})     | 99.79 (\pm{0.02})     | 99.59 (\pm{0.02})     | 1014791    |
|           | 1     | 94.81 (\pm{0.47})     | 86.42 (\pm{0.89})     | 90.41 (\pm{0.36})     | 41247      |
|           | Macro avg. | 97.10 (\pm{0.22}) | 93.10 (\pm{0.44})     | 95.00 (\pm{0.19})     | 103946    |

NPSC NorNe Binary Classification precision, recall and F1 metrics for all models. The 0 class denotes the Not Capital Letter class. The 1 class denotes the Capital letter class. The Support collumn refers to the number of entries for a given class. *729 sentences were dropped from SpaCy pipeline because of variance between prediction and gold standard sequence length.


