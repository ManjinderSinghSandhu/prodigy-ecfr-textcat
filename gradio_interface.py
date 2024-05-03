import gradio as gr
import jsonlines
import spacy

# Load the trained spaCy model
model_path = "./my_trained_model"
nlp = spacy.load(model_path)

# Load golden evaluation data
golden_eval_data = []
with jsonlines.open("data/goldenEval.jsonl") as f:
    for line in f:
        golden_eval_data.append(line)

# Function to evaluate text input
def evaluate_text(input_text):
    doc = nlp(input_text)
    # Perform evaluation logic here based on golden_eval_data and the model
    evaluation_result = "Evaluation result based on text input"  # Placeholder, adjust as needed
    return evaluation_result

# Function to evaluate file upload
def evaluate_file(upload):
    file_contents = upload.read().decode("utf-8")
    doc = nlp(file_contents)
    # Perform evaluation logic here based on golden_eval_data and the model
    evaluation_result = "Evaluation result based on uploaded file"  # Placeholder, adjust as needed
    return evaluation_result

# Create Gradio interface
text_input = gr.inputs.Textbox(lines=10, label="Input Text")
file_upload = gr.inputs.File(label="Upload File")
output_text = gr.outputs.Textbox(label="Evaluation Output")

# Define Gradio interface
interface = gr.Interface(
    fn=[evaluate_text, evaluate_file],
    inputs=[text_input, file_upload],
    outputs=output_text,
    title="spaCy Model Evaluator",
    description="Enter text or upload a file to evaluate using the trained spaCy model."
)

# Additional option to view evaluation print and download files
interface.launch(share=True)  # Launch the interface with the option to share
