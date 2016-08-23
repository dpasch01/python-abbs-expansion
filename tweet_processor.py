import sys
import re
import abbriviation_expansion

regexp = {"RT": "^RT", "MT": r"^MT", "ALNUM": r"(@[a-zA-Z0-9_]+)", "HASHTAG": r"(#[\w\d]+)", "URL": r"([https://|http://]?[a-zA-Z\d\/]+[\.]+[a-zA-Z\d\/\.]+)", "SPACES": r"\s+"}
regexp = dict((key, re.compile(value)) for key, value in regexp.items())

def removeUserHandles(tweet):
    return re.sub(regexp["ALNUM"], "", tweet)

def removeHashtags(tweet):
    return re.sub(regexp["HASHTAG"], "", tweet)

def removeURLs(tweet):
    return re.sub(regexp["URL"], "", tweet)
    return text

def process(text):
    text = removeURLs(text)
    text = removeHashtags(text)
    text = removeUserHandles(text)
    text = abbriviation_expansion.expand_abbs(text)
    return text

if __name__ == '__main__':
    text = process(sys.argv[1])
    print text
