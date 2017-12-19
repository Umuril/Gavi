import re
from nltk.corpus import stopwords

from .utils import *
from . import translate, fields

DEFAULT_INPUT_FILE = translate.DEFAULT_OUTPUT_FILE
DEFAULT_OUTPUT_FILE = 'out/matched'
DEFAULT_OUTPUT_TXT_FILE = 'out/matched.txt'
EN_STOPWORDS = stopwords.words('english')

def read_exhibitions(filename):
    exhibitions = []
    words_pattern = re.compile('\w+')

    with open(filename) as in_file:
        for line in in_file:
            exhibition = []
            for part in line.strip().lower().split(' : '):
                exhibition.append([word for word in words_pattern.findall(part)
                                   if word not in EN_STOPWORDS])
            exhibitions.append(exhibition)

    return exhibitions

@optional_input(DEFAULT_INPUT_FILE)
@optional_output(DEFAULT_OUTPUT_FILE, DEFAULT_OUTPUT_TXT_FILE)
def match(tweets):
    """Tries to tag each tweet with one exhibition"""

    exhibitions = read_exhibitions('txt/exhibitions.txt')
    print(exhibitions)
    out_tweets = []
    matched = False
    for tweet in tweets:
        text = tweet[fields.TEXT].lower()
        for place_tokens, name_tokens in exhibitions:
            place_similarity = (sum(x in text for x in place_tokens)/
                                len(place_tokens))
            name_similarity = (sum(x in text for x in name_tokens)/
                               len(name_tokens))
            if place_similarity*name_similarity > 1/3:
                tweet[' '.join(name_tokens)] = (place_similarity,
                                                name_similarity)
                matched = True

        if matched:
            out_tweets.append(tweet)
            matched = False

    return out_tweets

if __name__ == "__main__":
    import argparse as ap

    argparser = ap.ArgumentParser(description=match.__doc__)
    add_io_argparser(argparser, DEFAULT_INPUT_FILE, DEFAULT_OUTPUT_FILE,
                     DEFAULT_OUTPUT_TXT_FILE)
    args = argparser.parse_args()

    match(input_file=args.input_file, output_file=args.output_file,
          txt_file=args.txt_file)
