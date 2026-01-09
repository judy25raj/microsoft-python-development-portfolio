import json
import spacy
from typing import List, Dict

# Load spaCy model, download if needed
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Load medical data from JSON file
with open("medical_data.json", "r", encoding="utf-8") as f:
    medical_data = json.load(f)

# Base symptom list used for extraction
medical_knowledge_base = {
    "headache": "A pain in the head.",
    "fever": "Elevated body temperature.",
    "nausea": "Feeling of sickness with an inclination to vomit.",
    "cough": "A sudden expulsion of air from the lungs.",
    "fatigue": "Extreme tiredness resulting from mental or physical exertion."
}

def extract_symptoms(user_input: str) -> List[str]:
    """Extracts symptoms from user input using spaCy."""
    doc = nlp(user_input)
    extracted_symptoms: List[str] = []

    kb_symptoms = {symptom.lower(): desc for symptom, desc in medical_knowledge_base.items()}

    # Check tokens
    for token in doc:
        token_text = token.text.lower()
        if token_text in kb_symptoms and token_text not in extracted_symptoms:
            extracted_symptoms.append(token_text)

    # Check noun chunks (extension point for multi-word symptoms)
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.lower()
        if chunk_text in kb_symptoms and chunk_text not in extracted_symptoms:
            extracted_symptoms.append(chunk_text)

    return extracted_symptoms

def analyze_symptoms(extracted_symptoms: List[str]) -> Dict[str, int]:
    """Analyzes symptoms and returns possible conditions with counts."""
    possible_conditions: Dict[str, int] = {}
    symptoms_dict = medical_data.get("symptoms", {})

    for symptom in extracted_symptoms:
        if symptom in symptoms_dict:
            for condition in symptoms_dict[symptom]:
                if condition in possible_conditions:
                    possible_conditions[condition] += 1
                else:
                    possible_conditions[condition] = 1

    return possible_conditions

medical_recommendations = medical_data.get("recommendations", {})

def generate_response(extracted_symptoms: List[str], possible_conditions: Dict[str, int]) -> str:
    """Generates a response based on extracted symptoms and possible conditions."""
    response = ""
    if extracted_symptoms:
        response += "I understand you have " + ", ".join(extracted_symptoms) + "."
        response += "\nBased on your symptoms, the most likely possibilities are:\n"

        if possible_conditions:
            sorted_conditions = sorted(
                possible_conditions.items(),
                key=lambda item: item[1],
                reverse=True
            )
            for condition, count in sorted_conditions:
                response += f"- {condition} ({count} matching symptom(s))\n"
                if condition in medical_recommendations:
                    response += f"  * {medical_recommendations[condition]}\n"
                else:
                    response += "  * No specific recommendation available.\n"
        else:
            response += "I'm sorry, I don't recognize those symptoms in my knowledge base.\n"
    else:
        response = "I'm sorry, I didn't recognize any symptoms in your description.\n"

    response += (
        "Remember, I am just a chatbot and cannot provide definitive medical advice. "
        "Please consult a doctor for proper diagnosis and treatment."
    )
    return response

def run_chatbot():
    """Runs a simple multi-turn console chatbot session."""
    print("Welcome to the Medical Diagnosis Assistant Chatbot (Educational Demo).")
    print("Please describe your primary concern (e.g., 'I have a headache and nausea').")
    extracted_symptoms: List[str] = []

    user_input = input("You: ")
    extracted_symptoms = extract_symptoms(user_input)
    possible_conditions = analyze_symptoms(extracted_symptoms)
    response = generate_response(extracted_symptoms, possible_conditions)
    print("Chatbot:", response)

    while True:
        additional_symptoms = input("\nPlease enter an additional symptom, or 'no' if you have no more: ")
        if additional_symptoms.lower() in ("no", "nope", "none"):
            break

        new_symptoms = extract_symptoms(additional_symptoms)
        if new_symptoms:
            extracted_symptoms.extend(new_symptoms)
            possible_conditions = analyze_symptoms(extracted_symptoms)
            response = generate_response(extracted_symptoms, possible_conditions)
            print("Chatbot:", response)
        else:
            print("Chatbot: I didn't recognize that symptom. Please try again.")

    print("\nChatbot: Thank you for using the medical assistant demo. Take care!")

if __name__ == "__main__":
    run_chatbot()
