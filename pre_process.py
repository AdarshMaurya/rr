import nltk
import re
import spacy

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")

def remove_extra_spaces(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    processed_content = re.sub(r"\s+", " ", content)
    return processed_content


def write_processed_content(processed_content, output_filename):
    sentences = nltk.sent_tokenize(processed_content)
    with open(output_filename, "w", encoding="utf-8") as f:
        for sentence in sentences:
            if contains_company_name(sentence):
                f.write(sentence)
                f.write("\n")
            print(f"The sentence does not contain a company name: {sentence}")

def contains_company_name(sentence):
    doc = nlp(sentence)
    for ent in doc.ents:
        # Check if the entity is recognized as an organization (ORG)
        if ent.label_ == "ORG":
            return True
    return False

def check_company_names_in_file(file_path):
    # Open the file in read mode
    with open(file_path, "r") as file:
        # Read sentences separated by '\n'
        sentences = file.read().split("\n")

        # Check if each sentence contains a company name
        for sentence in sentences:
            if contains_company_name(sentence):
                print(f"The sentence contains a company name: {sentence}")
            else:
                print(f"The sentence does not contain a company name: {sentence}")


input_filename = "/Users/adarsh/Documents/Playground/LLM/research_equity/research_rating_data/changes/1937119.txt"
# input_filename = "/Users/adarsh/Documents/Playground/LLM/research_equity/research_rating_data/no-changes/2124986.txt"
output_filename = "test.txt"
processed_content = remove_extra_spaces(input_filename)
write_processed_content(processed_content, output_filename)
# check_company_names_in_file(output_filename)
