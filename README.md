# BABILong-ITA
This repository contains the BABILong-ITA dataset and the code for reproducing our LongMinerva results presented at CLiC-it 2025.

First download the dataset from [our server](http://corpora.ficlit.unibo.it/UploadDIR/babilong-ita.tgz) and uncompress it into the main folder.

To reproduce figures 2 and 3 from the paper, execute the evaluation of each single LLM, for example:
```
./evaluate_model.sh "google/gemma-3-4b-it" ./babilong-ita
```
To evaluate our LongMinerva solution based on [SelfExtend](https://github.com/datamllab/LongLM)

```
cd LongLM
./evaluate_model.sh "sapienzanlp/Minerva-7B-base-v1.0" ../babilong-ita
```

These scripts have been tested using:
- Python 3.10.16
- PyTorch 2.5.1
- CUDA 12.4
on a NVIDIA RTX A4000 and a NVIDIA L40.

If you use this dataset, please cite:

```
@InProceedings{Tamburini2025,
  author = {Tamburini, Fabio},
  title = {{BABILong-ITA: a new benchmark for testing Large Language Models effective context length and a Context Extension Method}},
  booktitle = {{Proceedings of the 11th Italian Conference on Computational Linguistics - CLIC-it 2025}},
  year = {2025},
  publisher = {CEUR-WS},
  location = {Cagliari, Italy},
}
```
