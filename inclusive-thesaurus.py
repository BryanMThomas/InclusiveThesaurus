import os
import csv
import json
import re
from nltk import download
from nltk.tokenize import word_tokenize

# Download the NLTK data needed for tokenization
download('punkt')

# Function to read the CSV file containing non-inclusive terms
def read_csv_file(file_path):
    non_inclusive_terms = {}

    # Open and read the CSV file
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # Iterate through each row in the CSV file
        for row in reader:
            term = row['non_inclusive_term'].lower()
            # Store the non-inclusive term along with its alternatives and reason
            non_inclusive_terms[term] = {
                'alternatives': row['inclusive_alternatives'],
                'reason': row['note']
            }

    return non_inclusive_terms

# Function to find non-inclusive terms in the input text
def find_non_inclusive_terms(text, terms_dict):
    found_terms = []
    added_terms = set()

    # Iterate through the terms dictionary
    for term in terms_dict:
        # Create a regex pattern to match the term
        pattern = r'\b' + re.escape(term) + r'\b'
        # Search for matches in the input text (case-insensitive)
        matches = list(re.finditer(pattern, text, re.IGNORECASE))

        # If matches are found and the term is not already added
        if matches and term not in added_terms:
            # Get the positions of the matches in the input text
            positions = [match.start() for match in matches]
            # Add the term, its positions, and related information to the found_terms list
            found_terms.append({'term': term, 'positions': positions, **terms_dict[term]})
            added_terms.add(term)

    return found_terms

# Main function
def main():
    # Read the CSV file containing non-inclusive terms
    csv_file_path = './inclusive-training-data.csv'
    non_inclusive_terms = read_csv_file(csv_file_path)

    # Get the input text from the environment variable or use the default text
    input_text = os.environ.get('INPUT_TEXT', "Your default input text goes here.")
    # Find non-inclusive terms in the input text
    found_terms = find_non_inclusive_terms(input_text, non_inclusive_terms)

    # Prepare the result and print it as a JSON string
    result = {'non-inclusive-terms': found_terms}
    print(json.dumps(result, indent=2))

# Entry point for the script
if __name__ == '__main__':
    main()
