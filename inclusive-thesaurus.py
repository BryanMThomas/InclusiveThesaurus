import csv
import os
from nltk.tokenize import word_tokenize
from nltk import download

# Download the NLTK data needed for tokenization
download('punkt')

def read_csv_file(file_path):
    non_inclusive_terms = set()

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            non_inclusive_terms.add(row['non_inclusive_term'].lower())

    return non_inclusive_terms

def find_non_inclusive_terms(text, terms_set):
    tokens = word_tokenize(text.lower())
    return [token for token in tokens if token in terms_set]

def main():
    csv_file_path = './inclusive-training-data.csv'
    non_inclusive_terms = read_csv_file(csv_file_path)

    input_text = os.environ.get('INPUT_TEXT', "Your default input text goes here.")
    found_terms = find_non_inclusive_terms(input_text, non_inclusive_terms)

    if found_terms:
        print("The following non-inclusive terms were found:", found_terms)
    else:
        print("No non-inclusive terms were found.")

if __name__ == '__main__':
    main()
