from transformers import pipeline

clf = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict_priority(description: str) -> str:
    result = clf(description)[0]
    label = result["label"].lower()

    if "neg" in label:
        return "high"
    return "medium"
