import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")


HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

CLASSIFY_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
REPLY_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-small"


def classify_lead(message):
    payload = {
        "inputs": message,
        "parameters": {
            "candidate_labels": ["Hot", "Warm", "Cold"]
        }
    }

    response = requests.post(CLASSIFY_URL, headers=HEADERS, json=payload)
    result = response.json()

    print("HF CLASSIFY RESPONSE:", result)

    # If API returns error
    if isinstance(result, dict) and "error" in result:
        return "Warm"

    # Correct response format (list of {label, score})
    if isinstance(result, list) and "label" in result[0]:
        return result[0]["label"]

    return "Warm"


def generate_reply(message):
    prompt = f"Write a polite professional reply to this customer inquiry:\n{message}"

    payload = {"inputs": prompt}
    response = requests.post(REPLY_URL, headers=HEADERS, json=payload)

    print("HF REPLY STATUS:", response.status_code)
    print("HF REPLY RAW TEXT:", response.text)

    # If empty response or error
    if response.status_code != 200 or not response.text:
        return "Thank you for your inquiry. Our team will contact you shortly."

    try:
        result = response.json()
    except Exception:
        return "Thank you for your inquiry. Our team will contact you shortly."

    if isinstance(result, list) and "generated_text" in result[0]:
        return result[0]["generated_text"]

    return "Thank you for your inquiry. Our team will contact you shortly."
