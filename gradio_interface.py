# Import necessary libraries
import gradio as gr
import spacy

# Load the trained spaCy model
model_path = "./my_trained_model"
nlp = spacy.load(model_path)

# Function to classify text
def classify_text(text):
    doc = nlp(text)
    predicted_labels = doc.cats
    return predicted_labels

# Function to save results to a file
def save_to_file(text, predicted_labels):
    with open("classification_results.txt", "w") as f:
        f.write("Text: {}\n\n".format(text))
        for label, score in predicted_labels.items():
            f.write("{}: {}\n".format(label, score))

# Gradio Interface
inputs = [
    gr.inputs.Textbox(lines=7, label="Enter your text"),
    gr.inputs.File(label="Upload a file")
]

output = gr.outputs.Textbox(label="Classification Results")

def classify_and_save(input_text, input_file):
    if input_text:
        text = input_text
    elif input_file:
        # Process the file and extract text
        with open(input_file.name, "r") as f:
            text = f.read()
    
    predicted_labels = classify_text(text)
    save_to_file(text, predicted_labels)
    return predicted_labels

iface = gr.Interface(fn=classify_and_save, inputs=inputs, outputs=output, title="Text Classifier")
iface.launch(share=True)
