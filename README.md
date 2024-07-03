<!-- WEASEL: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 Weasel Project: Citations of ECFR Banking Regulation in a spaCy pipeline.

Custom text classification project for spaCy v3 adapted from the spaCy v3

## https://huggingface.co/spaces/ManjinderUNCC/prodigy-ecfr-textcat

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[Weasel documentation](https://github.com/explosion/weasel).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`weasel run [name]`](https://github.com/explosion/weasel/tree/main/docs/cli.md#rocket-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `preprocess` | Execute the Python script `firstStep-format.py`, which performs the initial formatting of a dataset file for the first step of the project. This script extracts text and labels from a dataset file in JSONL format and writes them to a new JSONL file in a specific format.

Usage:
```
spacy project run preprocess
```

Explanation:
- The script `firstStep-format.py` reads data from the file specified in the `dataset_file` variable (`data/train200.jsonl` by default).
- It extracts text and labels from each JSON object in the dataset file.
- If both text and at least one label are available, it writes a new JSON object to the output file specified in the `output_file` variable (`data/firstStep_file.jsonl` by default) with the extracted text and label.
- If either text or label is missing in a JSON object, a warning message is printed.
- Upon completion, the script prints a message confirming the processing and the path to the output file.
 |
| `train-text-classification-model` | Train the text classification model for the second step of the project using the `secondStep-score.py` script. This script loads a blank English spaCy model and adds a text classification pipeline to it. It then trains the model using the processed data from the first step.

Usage:
```
spacy project run train-text-classification-model
```

Explanation:
- The script `secondStep-score.py` loads a blank English spaCy model and adds a text classification pipeline to it.
- It reads processed data from the file specified in the `processed_data_file` variable (`data/firstStep_file.jsonl` by default).
- The processed data is converted to spaCy format for training the model.
- The model is trained using the converted data for a specified number of iterations (`n_iter`).
- Losses are printed for each iteration during training.
- Upon completion, the trained model is saved to the specified output directory (`./my_trained_model` by default).
 |
| `classify-unlabeled-data` | Classify the unlabeled data for the third step of the project using the `thirdStep-label.py` script. This script loads the trained spaCy model from the previous step and classifies each record in the unlabeled dataset.

Usage:
```
spacy project run classify-unlabeled-data
```

Explanation:
- The script `thirdStep-label.py` loads the trained spaCy model from the specified model directory (`./my_trained_model` by default).
- It reads the unlabeled data from the file specified in the `unlabeled_data_file` variable (`data/train.jsonl` by default).
- Each record in the unlabeled data is classified using the loaded model.
- The predicted labels for each record are extracted and stored along with the text.
- The classified data is optionally saved to a file specified in the `output_file` variable (`data/thirdStep_file.jsonl` by default).
 |
| `format-labeled-data` | Format the labeled data for the final step of the project using the `finalStep-formatLabel.py` script. This script processes the classified data from the third step and transforms it into a specific format, considering a threshold for label acceptance.

Usage:
```
spacy project run format-labeled-data
```

Explanation:
- The script `finalStep-formatLabel.py` reads classified data from the file specified in the `input_file` variable (`data/thirdStep_file.jsonl` by default).
- For each record, it determines accepted categories based on a specified threshold.
- It constructs an output record containing the text, predicted labels, accepted categories, answer (accept/reject), and options with meta information.
- The transformed data is written to the file specified in the `output_file` variable (`data/train4465.jsonl` by default).
 |
| `evaluate-model` | Evaluate the trained model using the evaluation data and print the metrics.

Usage:
```
spacy project run evaluate-model
```

Explanation:
- The script `evaluate_model.py` loads the trained model and evaluates it using the golden evaluation data.
- It calculates evaluation metrics such as accuracy, precision, recall, and F1-score.
- The metrics are printed to the console.
 |
| `set-threshold` | Set the threshold for text categorization in a trained model.

Usage:
```
spacy project run set-threshold <model_path> <threshold>
```

Explanation:
- The script loads the trained model from the specified path.
- It sets the threshold for text categorization to the specified value.
 |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`weasel run [name]`](https://github.com/explosion/weasel/tree/main/docs/cli.md#rocket-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `train` | `preprocess` &rarr; `train-text-classification-model` &rarr; `classify-unlabeled-data` &rarr; `format-labeled-data` |
| `evaluate` | `set-threshold` &rarr; `evaluate-model` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`weasel assets`](https://github.com/explosion/weasel/tree/main/docs/cli.md#open_file_folder-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`data/firstStep_file.jsonl`](data/firstStep_file.jsonl) | Local | JSONL file containing formatted data from the first step |
| `data/five_examples_annotated5.jsonl` | Local | JSONL file containing five annotated examples |
| [`data/goldenEval.jsonl`](data/goldenEval.jsonl) | Local | JSONL file containing golden evaluation data |
| [`data/thirdStep_file.jsonl`](data/thirdStep_file.jsonl) | Local | JSONL file containing classified data from the third step |
| [`data/train.jsonl`](data/train.jsonl) | Local | JSONL file containing training data |
| [`data/train200.jsonl`](data/train200.jsonl) | Local | JSONL file containing initial training data |
| `data/train4465.jsonl` | Local | JSONL file containing formatted and labeled training data |
| [`python_Code/finalStep-formatLabel.py`](python_Code/finalStep-formatLabel.py) | Local | Python script for formatting labeled data in the final step |
| [`python_Code/firstStep-format.py`](python_Code/firstStep-format.py) | Local | Python script for formatting data in the first step |
| `python_Code/five_examples_annotated.ipynb` | Local | Jupyter notebook containing five annotated examples |
| [`python_Code/secondStep-score.py`](python_Code/secondStep-score.py) | Local | Python script for scoring data in the second step |
| [`python_Code/thirdStep-label.py`](python_Code/thirdStep-label.py) | Local | Python script for labeling data in the third step |
| `python_Code/train_eval_split.ipynb` | Local | Jupyter notebook for training and evaluation data splitting |
| [`data/firstStep_file.jsonl`](data/firstStep_file.jsonl) | Local | Python script for evaluating the trained model |
| [`README.md`](README.md) | Local | Markdown file containing project documentation |

<!-- WEASEL: AUTO-GENERATED DOCS END (do not remove) -->
