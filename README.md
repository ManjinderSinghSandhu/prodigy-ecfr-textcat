# prodigy-ecfr-textcat

https://huggingface.co/spaces/ManjinderUNCC/prodigy-ecfr-textcat

## About the Project

Our goal is to organize these financial institution rules and regulations so financial institutions  can go through newly created rules and regulations to know which departments to send the information to and to allow easy retrieval of these regulations when necessary. Text mining and information retrieval will allow a large step of the process to be automated. Automating these steps will allow less time and effort to be contributed for financial institutions employees. This allows more time and work to be used to accomplish other projects.

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Getting Started

Instructions on setting up the project on a local machine.

### Prerequisites

Before running the project, ensure you have the following software dependencies installed:
- [Python 3.x](https://www.python.org/downloads/)
- [spaCy](https://spacy.io/usage)
- [Prodigy](https://prodi.gy/docs/) (optional)

### Installation

Follow these step-by-step instructions to install and configure the project:

1. **Clone this repository to your local machine.**
```bash
git clone <https://github.com/ManjinderSinghSandhu/prodigy-ecfr-textcat.git>
```
2. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

3. Next, you need to have a Prodigy license key to use Prodigy. (But it's not required) Install Prodigy first:

```bash
python -m pip install prodigy==1.15.2 --extra-index-url https://$PRODIGY_KEY@download.prodi.gy
```

This assumes you previously set up your `PRODIGY_KEY` as an environmental variable like:

```bash
export PRODIGY_KEY=1111-1111-1111-1111
```

## Usage

To use the project, follow these steps:

1. **Prepare your data:**
   - Place your dataset files in the `/data` directory.
   - Optionally, annotate your data using Prodigy and save the annotations in the `/data` directory.

2. **Train the text classification model:**
   - Run the training script located in the `/python_Code` directory.

3. **Evaluate the model:**
   - Use the evaluation script to assess the model's performance on labeled data.

4. **Make predictions:**
   - Apply the trained model to new, unlabeled data to classify it into relevant categories.


## File Structure

Describe the organization of files and directories within the project.

- `/data`
  - `five_examples_annotated5.jsonl`
  - `goldenEval.jsonl`
  - `train.jsonl`
  - `train200.jsonl`
- `/python_Code`
  - `finalStep-formatLabel.py`
  - `firstStep-format.py`
  - `five_examples_annotated.ipynb`
  - `secondStep-score.py`
  - `thirdStep-label.py`
  - `gradio_interface.py`
- `requirements.txt`
- `requirements-dev.txt`
- `Project.yml`
- `README.md`

## License

- Package A: MIT License
- Package B: Apache License 2.0
- Prodigy 

