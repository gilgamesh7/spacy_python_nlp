# Test if correct package installed & language loaded

import spacy
nlp = spacy.load("en_core_web_sm") 
print(f"Language callable object : {nlp}")

# Doc Object for Processed Tex


# construct a Doc object. 
# A Doc object is a sequence of Token objects representing a lexical token.
introduction_doc = nlp(
    "This tutorial is about Natural Language Processing in spaCy."
)
print(f"Type of doc : {type(introduction_doc)}")

print(f"Tokens : {[token.text for token in introduction_doc]}")

