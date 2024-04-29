# prodigy-ecfr-textcat

Brief description of your project.

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About the Project

Our goal is to organize these financial institution rules and regulations so financial institutions  can go through newly created rules and regulations to know which departments to send the information to and to allow easy retrieval of these regulations when necessary. Text mining and information retrieval will allow a large step of the process to be automated. Automating these steps will allow less time and effort to be contributed for financial institutions employees. This allows more time and work to be used to accomplish other projects.

## Getting Started

Instructions on setting up the project on a local machine.

### Prerequisites

List any software dependencies or libraries required to run the project.

### Installation

Step-by-step instructions on how to install and configure the project.

## Usage

Explain how to use the project, including any command-line arguments, configurations, or examples.

## File Structure

Describe the organization of files and directories within the project.

- `/corpus`
  - `/labels`
    - `ner.json`
    - `parser.json`
    - `tagger.json`
    - `textcat_multilabel.json`
- `/data`
  - `eval.jsonl`
  - `firstStep_file.jsonl`
  - `five_examples_annotated5.jsonl`
  - `goldenEval.jsonl`
  - `thirdStep_file.jsonl`
  - `train.jsonl`
  - `train200.jsonl`
  - `train4465.jsonl`
- `/my_trained_model`
  - `/textcat_multilabel`
    - `cfg`
    - `model`
  - `/vocab`
    - `key2row`
    - `lookups.bin`
    - `strings.json`
    - `vectors`
    - `vectors.cfg`
  - `config.cfg`
  - `meta.json`
  - `tokenizer`
- `/output`
  - `/experiment1`
    - `/model-best`
      - `/textcat_multilabel`
        - `cfg`
        - `model`
      - `/vocab`
        - `key2row`
        - `lookups.bin`
        - `strings.json`
        - `vectors`
        - `vectors.cfg`
      - `config.cfg`
      - `meta.json`
      - `tokenizer`
    - `/model-last`
      - `/textcat_multilabel`
        - `cfg`
        - `model`
      - `/vocab`
        - `key2row`
        - `lookups.bin`
        - `strings.json`
        - `vectors`
        - `vectors.cfg`
      - `config.cfg`
      - `meta.json`
      - `tokenizer`
  - `/experiment3`
    - `/model-best`
      - `/textcat_multilabel`
        - `cfg`
        - `model`
      - `/vocab`
        - `key2row`
        - `lookups.bin`
        - `strings.json`
        - `vectors`
        - `vectors.cfg`
      - `config.cfg`
      - `meta.json`
      - `tokenizer`
    - `/model-last`
      - `/textcat_multilabel`
        - `cfg`
        - `model`
      - `/vocab`
        - `key2row`
        - `lookups.bin`
        - `strings.json`
        - `vectors`
        - `vectors.cfg`
      - `config.cfg`
      - `meta.json`
      - `tokenizer`
- `/python_Code`
  - `finalStep-formatLabel.py`
  - `firstStep-format.py`
  - `five_examples_annotated.ipynb`
  - `secondStep-score.py`
  - `thirdStep-label.py`
  - `train_eval_split.ipynb`
- `Project3TerminalCode.txt`
- `README.md`
- `prodigy.json`



## Contributing

Guidelines for contributing to the project, including how to report bugs or suggest improvements.

## License

Specify the project's license (e.g., MIT License, Apache License 2.0).

## Acknowledgements

Credits to any individuals, organizations, or resources that contributed to the project.
