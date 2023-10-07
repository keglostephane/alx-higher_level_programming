#!/usr/bin:python3
def multiple_returns(sentence):
    if sentence is not None:
        if not sentence:
            return 0, None
        else:
            length = len(sentence)
            return length, sentence[0]
