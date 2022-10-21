# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(stack1, stack2, stack3):
    # write your code in Python 3.8.10
    ans = ''
    if not stack1:
        stack1.append(0)
    if not stack2:
        stack2.append(0)
    if not stack3:
        stack3.append(0)
        
    while stack1 and stack2 and stack3 and any(stack1+stack2+stack3):
        target = max(stack1[-1], stack2[-1], stack3[-1])
        if target == stack1[-1]:
            ans += '1'
            stack1.pop()
            if not stack1:
                stack1.append(0)
        elif target == stack2[-1]:
            ans += '2'
            stack2.pop()
            if not stack2:
                stack2.append(0)
        elif target == stack3[-1]:
            ans += '3'
            stack3.pop()
            if not stack3:
                stack3.append(0)
    return ans


import spacy
import re
nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    doc = nlp(sentences)
    for word in doc.ents:
        if word.label_ == 'PERSON':
            sentences = re.sub(word.text, 'X'*len(word.text),sentences, 1)
        
    return sentences

