# Master thesis Named Entity Recognition in Speech to Text Transcripts
Master thesis on Proper Capitalization in Speech to Text Transcripts using NER
&ensp;
This repository contain code and results from the conducted experiments.
&ensp;
## Abstract
Traditionally, named entity recognition (NER) research use properly capitalized data for training in testing, however, these results give little insight to how these models may perform in scenarios where proper capitalization is not in place. In this thesis, we explore the capabilities of five fine-tuning BERT based models for NER in all lowercase text. Furthermore, the aim is to measure the performance for classify named entity types correctly, as well as just simply detecting that a named entity is present, so a capitalization error may be corrected. The performance will be assessed using all lowercase data from the NorNE dataset, and the Norwegian Parliamentary Speech Corpus.
&ensp;
&ensp;
## Some results from the experimets

### NorNE results
|    Model    | No Boundary | Strict Match | Binary |
|------------|-------------|--------------|--------|
|   SpaCy*   |    50.87    |    45.89     |  80.17 |
|   NCRF++   |    42.33    |    32.20     |  73.66 |
|   mBERT    | 82.15 (±0.50)| 79.97 (±0.41)| 95.51 (±0.56) |
|  NorBERT   | 83.12 (±1.10)| 82.19 (±1.26)| 96.32 (±0.10) |
| NorBERT2   | 85.45 (±0.23)| 84.38 (±0.37)| 95.32 (±0.08) |
|  NB-BERT   | 87.00 (±0.30)| 86.50 (±0.34)| 97.06 (±0.09) |
| Ner-Scandi | **87.06** (±0.56)| **86.58** (±0.45)| **97.07** (±0.13) |


NorNE results for all models. BERT models use the average F1 across all seeds
for a given model. No Boundary refers to NER without named entity token span taken into
account. Strict Match refers to NER with named entity token span taken into the evaluation.
Binary classification denotes the task where only the detection if an entity is present, without
specific type associated. *Ten sentences were dropped from SpaCy pipeline


### NPSC binary results

TBA 
|   Model   | Class |  Precision  |   Recall   |    F1    |  Support   |
|-----------|-------|-------------|------------|----------|------------|
|  Spacy*   |   0   |    99.76    |    98.28   |  99.02   |  1013745   |
|           |   1   |    57.27    |    90.77   |  70.23   |   25723    |
|           |Macro avg.|    78.51    |    94.52   |  84.62   |  1039468   |
|------------|-------|-----------------|-----------------|-----------------|------------|
|   NCRF++  |   0   |    97.38    |    99.77   |  98.56   |  1014791   |
|           |   1   |    85.85    |    34.04   |  48.75   |   41247    |
|           |Macro avg.|    91.61    |    66.91   |  73.66   |  1056038 
|------------|-------|-----------------|-----------------|-----------------|------------||
|   mBERT   |   0   | 99.41 (±0.06)| 99.64 (±0.03)| 99.52 (±0.02)|  1014791   |
|           |   1   | 91.09 (±0.70)| 86.18 (±1.19)| 88.56 (±0.39)|   41247    |
|           |Macro avg.| 95.25 (±0.32)| 92.91 (±0.58)| 94.04 (±0.20)|  1039468 
|------------|-------|-----------------|-----------------|-----------------|------------|
|  NorBERT  |   0   | 99.41 (±0.11)| 99.74 (±0.04)| 99.58 (±0.04)|  1014791   |
|           |   1   | 93.69 (±1.04)| 86.64 (±1.97)| 90.00 (±0.66)|   41247    |
|           |Macro avg.| 96.55 (±0.47)| 93.19 (±0.97)| 94.79 (±0.35)|  1039468   |
|------------|-------|-----------------|-----------------|-----------------|------------|
| NorBERT2  |   0   | 99.39 (±0.05)| 99.79 (±0.02)| 99.59 (±0.02)|  1014791   |
|           |   1   | 94.81 (±0.47)| 86.42 (±0.89)| 90.41 (±0.36)|   41247    |
|           |Macro avg.| 97.10 (±0.22)| 93.10 (±0.44)| 95.00 (±0.19)|  1039468 
|------------|-------|-----------------|-----------------|-----------------|------------|
|   NB-BERT  |   0   | 99.35 (±0.04)   | 99.85 (±0.02)   | 99.59 (±0.02)   |  1014791   |
|            |   1   | 96.22 (±0.47)   | 85.66 (±0.78)   | 90.63 (±0.43)   |   41247    |
|            |Macro avg.| 97.78 (±0.23)   | 92.76 (±0.39)   | 95.11 (±0.23)   |  1039468   |
|------------|-------|-----------------|-----------------|-----------------|------------|
| Scandi-ner |   0   | 99.42 (±0.05)   | 99.82 (±0.02)   | 99.62 (±0.02)   |  1014791   |
|            |   1   | 95.71 (±0.39)   | 87.03 (±0.97)   | 91.16 (±0.43)   |   41247    |
|            |Macro avg.| 97.56 (±0.18)   | 93.43 (±0.48)   | 95.39 (±0.23)   |  1039468   |

NPSC NorNe Binary Classification precision, recall and F1 metrics for all models. 0 class denotes the Not Capital Letter class. 1 class denotes the Capital Letter class. The Support collumn refers to the number of entries for a given class. *729 sentences were dropped from SpaCy pipeline because of difference prediction sequence length and gold standard sequence length







&ensp;&ensp;&ensp;
&ensp;
&ensp;
Link to the NorNE dataset: https://github.com/ltgoslo/norne
Link to the Norwegian Parliamentary Speech Corpus: https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-58/




