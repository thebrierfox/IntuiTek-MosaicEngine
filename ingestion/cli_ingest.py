import sys
import json
from concept_ingestion import analyze_concept

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli_ingest.py <path_to_concept_text_file>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    with open(input_path, "r") as f:
        concept_text = f.read()
    
    try:
        result = analyze_concept(concept_text)
        output_path = "output_concept.json"
        with open(output_path, "w") as out:
            json.dump(result, out, indent=4)
        print(f"Concept analysis successful. Output written to {output_path}")
    except Exception as e:
        print(f"Error during concept analysis: {e}")

if __name__ == "__main__":
    main()
