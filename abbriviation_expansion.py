import pickle
import string
import sys

def expand_abbs(text):
    with open('abbs.pickle', 'rb') as handle:
      dic = pickle.load(handle)

    text = text.lower()
    text = " ".join(text.split())
    for word in text.split():
        puncs = set(string.punctuation)
        word = ''.join(ch for ch in word if ch not in puncs)
        replace_word = dic.get(word)

        if replace_word != None:
            text = text.replace(word, replace_word)

    return text

if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = expand_abbs(sys.argv[1])
    else:
        text = "Must provide a text to expand."
    print text
