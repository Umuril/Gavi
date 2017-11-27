import re

from .util import *

DEFAULT_INPUT_FILE = 'txt/mini_mostre.txt'
DEFAULT_OUTPUT_FILE = 'out/extracted.pkl'
DEFAULT_OUTPUT_TXT_FILE = 'txt/extracted.txt'
DEFAULT_FIELDS = ('TextTW', 'Lang')

@save_to_txt(DEFAULT_OUTPUT_TXT_FILE)
def extract(fields = DEFAULT_FIELDS, filename = DEFAULT_INPUT_FILE, output = DEFAULT_OUTPUT_FILE):
    """Extracts only valuable fields from the tweets"""

    # Pattern used to split the file in single tweet's block of
    # information. A block is identified by two newline characters
    # followed by a field name or by the end of the string.
    split_pattern = re.compile(r'\n\n(?=[A-z_-]+ : |\Z)')
    # Pattern used to extract only some fields.
    # It matches both the field name and the content.
    # The content matches every character that is not the next field
    # or the end of the string.
    fields_pattern = re.compile(r'(^' +
                                '|'.join(fields) +
                                ') : (.+?)(?=\n+[A-z_-]+ : |\Z)',
                                re.MULTILINE | re.DOTALL)
    
    tweets = []
    with open(filename) as in_file:
        for tweet_info in split_pattern.split(in_file.read()):
            tweet = dict(fields_pattern.findall(tweet_info))
            if tweet:
                tweets.append(tweet)

    dump_tweets(tweets, output)
    # if txt:
    #     write_tweets_txt(tweets, DEFAULT_OUTPUT_TXT_FILE if txt == True else txt)
    return tweets

if __name__ == "__main__":
    import argparse as ap

    argparser = ap.ArgumentParser(description=extract.__doc__)
    argparser.add_argument('-f', '--fields', nargs='+',
                           default=DEFAULT_FIELDS,
                           help='fields to be extracted')
    add_io_argparser(argparser, DEFAULT_INPUT_FILE, DEFAULT_OUTPUT_FILE,
                     DEFAULT_OUTPUT_TXT_FILE)
    args = argparser.parse_args()

    tweets = extract(args.fields, args.in_file.name, args.out_file.name, txt = args.txt_file.name if args.txt_file else None)