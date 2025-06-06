# Towards Optimizing the Retrieval Quality of a Retrieval-Augmented Chatbot for HPC User Support

This repository contains code and data for the master's thesis "Towards
Optimizing the Retrieval Quality of a Retrieval-Augmented Chatbot for HPC User
Support".

## Contents

### Data

The `./csc-services-qa` directory contains code for building a question
answering dataset about CSC and LUMI computing services. The directory
contains instructions for building the dataset. The final dataset
is provided as `./csc-services-qa/csc-services-qa/csc_services_qa.json`.

### Experiments

The `./experiments` directory contains code for building RAG systems,
evaluating them on the QA dataset, and analyzing the results.

### Thesis

The thesis document is provided as `./Sainio_Mitja_Mastersthesis_2025.pdf`.

## Licensing

This project is licensed under the MIT License. It includes [BARTScore](https://github.com/neulab/BARTScore),
which is licensed under the Apache License 2.0.