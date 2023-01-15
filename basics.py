# Test if correct package installed & language loaded

import spacy
from pathlib import Path 


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

# Read from a file
file_name = Path.cwd()/"documents"/"example.txt"
introduction_doc = nlp(
    file_name.read_text(encoding="utf-8")
)

print(f"Tokens : {[token.text for token in introduction_doc]}")

# Identify sentences
sentences = list(introduction_doc.sents)
print(f"Number of sentences : {len(sentences)}")
print(f"The sentences are : \n {[sentence for sentence in sentences]}")

# Custom sentence seperators
ellipsis_text = (
    "Gus, can you, ... never mind, I forgot"
    " what I was saying. So, do you think"
    " we should ..."
)
from spacy.language import Language
@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    """Add support to use `...` as a delimiter for sentence detection"""
    for token in doc[:-1]:
        if token.text == "...":
            doc[token.i + 1].is_sent_start = True
    return doc

custom_nlp = spacy.load("en_core_web_sm")
custom_nlp.add_pipe("set_custom_boundaries", before="parser")
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
for sentence in custom_ellipsis_sentences:
    print(sentence)

# Get token index
about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)

# Atributes
print(
    f"{'Text with Whitespace':22}"
    f"{'Is Alphanumeric?':15}"
    f"{'Is Punctuation?':18}"
    f"{'Is Stop Word?'}"
)

for token in about_doc:
    print(
        f"{str(token.text_with_ws):22}" 
        f"{str(token.is_alpha):15}" 
        f"{str(token.is_punct):18}" 
        f"{str(token.is_stop)}" 
    )
