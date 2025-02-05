import os
import json
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key securely from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY is not set. Please set it in your .env file.")

openai.api_key = OPENAI_API_KEY

def analyze_concept(concept_text):
    prompt = (
        "Extract the core components, functionalities, and data structures "
        "from the following concept blueprint:\n\n" + concept_text +
        "\n\nReturn a JSON structure with keys: 'modules', 'databases', 'interfaces', and 'workflows'."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in system architecture."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
    except Exception as e:
        raise RuntimeError(f"OpenAI API call failed: {e}")

    try:
        structured_concept = json.loads(response['choices'][0]['message']['content'])
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to decode LLM response: {e}")
    return structured_concept

if __name__ == "__main__":
    # For testing purposes, allow CLI input
    with open("sample_concept.txt", "r") as f:
        concept_text = f.read()
    result = analyze_concept(concept_text)
    with open("output_concept.json", "w") as out:
        json.dump(result, out, indent=4)
