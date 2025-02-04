import openai
import json

def analyze_concept(concept_text):
    prompt = (
        "Extract the core components, functionalities, and data structures "
        "from the following concept blueprint:\n\n" + concept_text +
        "\n\nReturn a JSON structure with keys: 'modules', 'databases', 'interfaces', and 'workflows'."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in system architecture."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    structured_concept = json.loads(response['choices'][0]['message']['content'])
    return structured_concept

if __name__ == "__main__":
    with open("sample_concept.txt", "r") as f:
        concept_text = f.read()
    result = analyze_concept(concept_text)
    with open("output_concept.json", "w") as out:
        json.dump(result, out, indent=4)

