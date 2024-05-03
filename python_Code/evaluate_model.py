import jsonlines
import spacy
from sklearn.metrics import classification_report, accuracy_score, f1_score, precision_score, recall_score

# Load the trained spaCy model
model_path = "./my_trained_model"
nlp = spacy.load(model_path)

# Load the golden evaluation data
golden_eval_data = []
with jsonlines.open("data/goldenEval.jsonl") as reader:
    for record in reader:
        golden_eval_data.append(record)

# New threshold for considering a label
new_threshold = 0.21  # Change this to your desired threshold value

# Predict labels for each record using your model with the new threshold
predicted_labels = []
for record in golden_eval_data:
    text = record["text"]
    doc = nlp(text)
    # Apply the new threshold to the predicted labels
    filtered_labels = {label: score for label, score in doc.cats.items() if score > new_threshold}
    predicted_labels.append(filtered_labels)

# Extract ground truth labels from the golden evaluation data
true_labels = [record["accept"] for record in golden_eval_data]

# Convert label format to match sklearn's classification report format
true_labels_flat = [label[0] if label else "reject" for label in true_labels]
predicted_labels_flat = [max(pred, key=pred.get) if pred else "reject" for pred in predicted_labels]

# Calculate evaluation metrics
accuracy = accuracy_score(true_labels_flat, predicted_labels_flat)
precision = precision_score(true_labels_flat, predicted_labels_flat, average='weighted')
recall = recall_score(true_labels_flat, predicted_labels_flat, average='weighted')
f1 = f1_score(true_labels_flat, predicted_labels_flat, average='weighted')

# Additional classification report
report = classification_report(true_labels_flat, predicted_labels_flat)

# Print or save the evaluation metrics
print("Evaluation Metrics:")
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")

# Print or save the detailed classification report
print("Detailed Classification Report:")
print(report)
