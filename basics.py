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

# Default tokensiation
custom_about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London@based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)

print([token.text for token in nlp(custom_about_text)])
# Custom token
import re
from spacy.tokenizer import Tokenizer
custom_nlp = spacy.load("en_core_web_sm")
prefix_re = spacy.util.compile_prefix_regex(
    custom_nlp.Defaults.prefixes
)
suffix_re = spacy.util.compile_suffix_regex(
    custom_nlp.Defaults.suffixes
)
custom_infixes = [r"@"]
infix_re = spacy.util.compile_infix_regex(
    list(custom_nlp.Defaults.infixes) + custom_infixes
)
custom_nlp.tokenizer = Tokenizer(
    nlp.vocab,
    prefix_search=prefix_re.search,
    suffix_search=suffix_re.search,
    infix_finditer=infix_re.finditer,
    token_match=None,
)
custom_tokenizer_about_doc = custom_nlp(custom_about_text)
print([token.text for token in custom_tokenizer_about_doc[8:15]])

# Stop words
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
print(f"Printing 10 out of {len(list(spacy_stopwords))} stop words : ")
for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)

# Lemmatization is the process of reducing inflected forms of a word 
# while still ensuring that the reduced form belongs to the language. 
# This reduced form, or root word, is called a lemma.
print("\n Lemmatization : ")
conference_help_text = (
    "Gus is helping organize a developer"
    " conference on Applications of Natural Language"
    " Processing. He keeps organizing local Python meetups"
    " and several internal talks at his workplace."
)
conference_help_doc = nlp(conference_help_text)
print("Print all lemmas : ")
for token in conference_help_doc:
    print(str(token.lemma_))
print("Print tokens tht have been lemmatized : ")
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")
