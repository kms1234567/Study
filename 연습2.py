import spacy

nlp = spacy.load('en_core_web_md')
text = 'Yuh-jung Youn won the Oscar for best supporting actress for her performance in "Minari" on Sunday and made history by becoming the first Korean actor to win an Academy Award.'
doc = nlp(text)

str_format = "{:>10}"*8
print(str_format.format('Text', 'Lemma', 'POS', 'Tag', 'Dep', 'Shape', 'is alpha', 'is stop'))
print("=="*40)

for token in doc:
    print(str_format.format(token.text, token.lemma_, token.pos_, token.tag_, 
                            token.dep_, token.shape_, str(token.is_alpha), str(token.is_stop)))