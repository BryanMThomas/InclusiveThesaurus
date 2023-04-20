import os
import csv
import json
import re
from nltk import download
from nltk.tokenize import word_tokenize

# Download the NLTK data needed for tokenization
download('punkt')

def read_csv_file(file_path):
    non_inclusive_terms = {}

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            term = row['non_inclusive_term'].lower()
            non_inclusive_terms[term] = {
                'alternatives': row['inclusive_alternatives'],
                'reason': row['note']
            }

    return non_inclusive_terms

def find_non_inclusive_terms(text, terms_dict):
    found_terms = []
    added_terms = set()

    for term in terms_dict:
        pattern = r'\b' + re.escape(term) + r'\b'
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        
        if matches and term not in added_terms:
            positions = [match.start() for match in matches]
            found_terms.append({'term': term, 'positions': positions, **terms_dict[term]})
            added_terms.add(term)

    return found_terms

def main():
    csv_file_path = './inclusive-training-data.csv'
    non_inclusive_terms = read_csv_file(csv_file_path)

    input_text = os.environ.get('INPUT_TEXT', "Your default input text goes here.")
    found_terms = find_non_inclusive_terms(input_text, non_inclusive_terms)

    result = {'non-inclusive-terms': found_terms}
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
