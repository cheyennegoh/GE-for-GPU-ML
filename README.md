# GE for GPU ML

GE for GPU ML implements a toolchain for evolving CUDA kernels using grammatical evolution [(Ryan et al., 1998)](https://doi.org/10.1007/BFb0055930). This approach is applied to the intertwined sprials problem [(Lang and Witbrock, 1988)](http://dx.doi.org/10.13140/2.1.3459.2329) and the DRIVE (Digital Retinal Images for Vessel Extraction) dataset [(Staal et al., 2004)](https://doi.org/10.1109/TMI.2004.825627).

This project was developed by Cheyenne Goh as part of the dissertation *Evolving Machine Learning GPU Programs for Image Segmentation by Grammatical Evolution*, for the degree "MSc in Artificial Intelligence and Machine Learning" at the University of Limerick.

## Setup

Install dependencies:

`pip install -r requirements.txt`

Update GRAPE submodule:

`git submodule update --init --recursive`

## Usage

Run optimiser:

`python optimiser.py`

Run GE:

`python ge.py`

Run analysis:

`python analysis.py -i path/to/results`

## Help

Use the `-h` or `--help` option to view all possible options.