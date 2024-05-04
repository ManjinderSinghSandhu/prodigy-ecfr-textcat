import spacy

def set_threshold(model_path, threshold):
    # Load the trained model
    nlp = spacy.load(model_path)

    # Set the threshold for text classification
    nlp.get_pipe('textcat_multilabel').threshold = threshold

    return nlp

# Example usage:
if __name__ == "__main__":
    model_path = "./my_trained_model"
    threshold = 0.21
    nlp = set_threshold(model_path, threshold)
