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

# Function to evaluate the predicted labels for the input text
def evaluate_text(input_text):
    # Get the predicted labels and probabilities for the input text
    doc = nlp(input_text)
    predicted_labels = doc.cats
    
    # Construct output dictionary with likelihood for each label
    output_dict = {
        "PredictedLabels": {label: score for label, score in predicted_labels.items()}
    }
    
    return output_dict

# Gradio Interface
iface = gr.Interface(fn=evaluate_text, inputs="text", outputs="json", title="Text Evaluation-Manjinder", description="Enter your text")
iface.launch(share=True)

# import gradio as gr
# import spacy
# from sklearn.metrics import classification_report, accuracy_score, f1_score, precision_score, recall_score

# # Load the trained spaCy model
# model_path = "./my_trained_model"
# nlp = spacy.load(model_path)

# # Threshold for classification
# threshold = 0.21

# # Function to classify text
# def classify_text(text):
#     doc = nlp(text)
#     predicted_labels = doc.cats
#     return predicted_labels

# # Function to evaluate the predicted labels for the input text
# def evaluate_text(input_text):
#     # Get the predicted labels and probabilities for the input text
#     doc = nlp(input_text)
#     predicted_labels = doc.cats
    
#     # Assuming you have ground truth labels for the input text, you would compare the predicted labels with the ground truth labels here.
#     # For demonstration purposes, let's assume the ground truth labels are provided here.
#     ground_truth_labels = {
#         "CapitalRequirements": 0,
#         "ConsumerProtection": 1,
#         "RiskManagement": 0,
#         "ReportingAndCompliance": 1,
#         "CorporateGovernance": 0
#     }

#     # Convert predicted and ground truth labels to lists
#     predicted_labels_list = [predicted_labels[label] for label in ground_truth_labels]
#     ground_truth_labels_list = [ground_truth_labels[label] for label in ground_truth_labels]

#     # Calculate evaluation metrics
#     accuracy = accuracy_score(ground_truth_labels_list, [1 if prob > threshold else 0 for prob in predicted_labels_list])
#     precision = precision_score(ground_truth_labels_list, [1 if prob > threshold else 0 for prob in predicted_labels_list], average='weighted')
#     recall = recall_score(ground_truth_labels_list, [1 if prob > threshold else 0 for prob in predicted_labels_list], average='weighted')
#     f1 = f1_score(ground_truth_labels_list, [1 if prob > threshold else 0 for prob in predicted_labels_list], average='weighted')

#     # Additional classification report
#     report = classification_report(ground_truth_labels_list, [1 if prob > threshold else 0 for prob in predicted_labels_list])

#     # Construct output dictionary
#     output_dict = {
#         "PredictedLabels": predicted_labels,
#         "EvaluationMetrics": {
#             "Accuracy": accuracy,
#             "Precision": precision,
#             "Recall": recall,
#             "F1-Score": f1,
#             "ClassificationReport": report
#         }
#     }
    
#     return output_dict

# # Gradio Interface
# iface = gr.Interface(fn=evaluate_text, inputs="text", outputs="json", title="Text Evaluation-Manjinder", description="Enter your text")
# iface.launch(share=True)
