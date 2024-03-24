# Welcome to the personalization-experiment pipeline 

The goal of this pipeline is to enable users to prepare the dataset for the task, run the training process and make predictions with our trained models

## Installation
### using pip
### using poetry

## Commands as a python library (as a cli just remove python3 -m)

* `python3 -m personal-learner dataset create [dir-name]` - preprocess the dataset from a given folder with the raw files.
* `python3 -m personal-learner model train [dir-name]` - train a new model given an folder architecture and a data folder 
* `python3 -m personal-learner predict [inputs-file]` - predict masked sentences given a txt file with one masked sentence per line 
* `python3 -m personal-learner -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        datasets.md  # The documentation of creating/processing datasets.
        	- datasets_create.md  # The documentation of.
        ...       # Other markdown pages, images and other files.
