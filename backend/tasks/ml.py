def predict_priority(text):
    text = text.lower()

    high_keywords = ['urgent', 'asap', 'bug', 'error', 'fail', 'crash']
    medium_keywords = ['soon', 'important', 'update', 'refactor']

    for word in high_keywords:
        if word in text:
            return 'high'

    for word in medium_keywords:
        if word in text:
            return 'medium'

    return 'low'

