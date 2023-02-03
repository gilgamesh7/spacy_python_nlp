# Named-Entity Recognition
# Named-entity recognition (NER) is the process of locating 
# named entities in unstructured text 
# and then classifying them into predefined categories, 
# such as person names, organizations, locations, monetary values, percentages, and time expressions.

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

piano_class_text = (
    "Great Piano Academy is situated"
    " in Mayfair or the City of London and has"
    " world-class piano instructors."
)
piano_class_doc = nlp(piano_class_text)

for ent in piano_class_doc.ents:
    print(
        f"""
            {ent.text = }
            {ent.start_char = }
            {ent.end_char = }
            {ent.label_ = }
            spacy.explain('{ent.label_}') = {spacy.explain(ent.label_)}
            """
        )

displacy.serve(piano_class_doc, style="ent", port=5004)
