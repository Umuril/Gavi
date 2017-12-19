import itertools as it

from .utils import *
from . import extract, fields

DEFAULT_INPUT_FILE = extract.DEFAULT_OUTPUT_FILE
DEFAULT_OUTPUT_FILE = 'out/no_duplicates'
DEFAULT_OUTPUT_TXT_FILE = 'out/no_duplicates.txt'

@optional_input(DEFAULT_INPUT_FILE)
@optional_output(DEFAULT_OUTPUT_FILE, DEFAULT_OUTPUT_TXT_FILE)
def remove_duplicates(tweets):
    """Remove duplicates (retweets) and keep the maximum retweet count
       for each one"""

    out_tweets = []
    text_keyfunc = lambda x: x[fields.TEXT]
    tweets = sorted(tweets, key=text_keyfunc)
    for text, group in it.groupby(tweets, text_keyfunc):
        out_tweets.append(
            max(group, key=lambda x: int(x.get(fields.RETWEET_COUNT, 0))))

    return out_tweets
        

if __name__ == "__main__":
    import argparse as ap

    argparser = ap.ArgumentParser(description=remove_duplicates.__doc__)
    add_io_argparser(argparser, DEFAULT_INPUT_FILE, DEFAULT_OUTPUT_FILE,
                     DEFAULT_OUTPUT_TXT_FILE)
    args = argparser.parse_args()

    remove_duplicates(input_file=args.input_file,
                      output_file=args.output_file,
                      txt_file=args.txt_file)
