# InclusiveThesaurus

## Project Goal

InclusiveThesaurus is a Python-based Machine Learning (ML) API designed to detect non-inclusive language and suggest inclusive alternatives. The project leverages Azure ML Studio to enhance language sensitivity across various categories.

## Current Implementation
The current implementation is a rule-based system that processes input text and employs regular expressions (regex) to match against a curated dataset of non-inclusive terms. The API returns a JSON response containing the detected non-inclusive terms, their inclusive alternatives, and an explanation of why the alternative is valuable and more inclusive.

## In Progress
We are working on integrating an advanced machine learning model that excels at understanding and processing input text. Our aim is to fine-tune this model to effectively identify non-inclusive terms using the curated dataset, thereby enhancing the API's performance and accuracy in promoting inclusive language.