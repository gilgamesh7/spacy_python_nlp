import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

# Tree and Subtree Navigation
one_line_about_text = (
    "Gus Proto is a Python developer"
    " currently working for a London-based Fintech company"
)
one_line_about_doc = nlp(one_line_about_text)

print(f"All Tokens : \n {[token.text for token in one_line_about_doc]}")

print(f"children of developer : \n {[token.text for token in one_line_about_doc[5].children]}")

print(f"previous neighboring node of developer : \n {one_line_about_doc[5].nbor(-1)}")

print(f"next neighboring node of developer : \n {one_line_about_doc[5].nbor()}")

print(f"all tokens on the left of developer : \n {[token.text for token in one_line_about_doc[5].lefts]}")

print(f"all tokens on the right of developer : \n {[token.text for token in one_line_about_doc[5].rights]}")

print(f"subtree of developer : \n {list(one_line_about_doc[5].subtree)}")



# displacy.serve(one_line_about_doc, style="dep", port=5003)