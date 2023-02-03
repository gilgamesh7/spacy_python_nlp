# Dependency Parsing Using spaCy
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

# piano_text = "Gus is learning piano"
piano_text = "Fear, O Achilles, the wrath of heaven; think on your own father and have compassion upon me, who am the more pitiable, for I have steeled myself as no man yet has ever steeled himself before me, and have raised to my lips the hand of him who slew my son."
piano_doc = nlp(piano_text)
for token in piano_doc:
    print(
        f"""
            TOKEN: {token.text}
            =====
            {token.tag_ = }
            {token.head.text = }
            {token.dep_ = }
        """
    )

displacy.serve(piano_doc, style="dep", port=5003)