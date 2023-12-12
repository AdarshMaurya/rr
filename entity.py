import spacy

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")


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


# Example usage
file_path = "test.txt"
check_company_names_in_file(file_path)
