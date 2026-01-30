from nlp.summarizer import summarize
from nlp.ner import extract_entities

def detect_topic(text):
    text = text.lower()
    if any(word in text for word in ["match", "goal", "player", "football", "score"]):
        return "sports"
    elif any(word in text for word in ["election", "government", "president", "policy"]):
        return "politics"
    elif any(word in text for word in ["technology", "ai", "software", "computer"]):
        return "tech"
    else:
        return "general"

def full_pipeline(text, length="medium"):
    topic = detect_topic(text)
    summary = summarize(text, length)
    entities = extract_entities(text)

    return {
        "topic": topic,
        "summary": summary,
        "entities": entities
    }
