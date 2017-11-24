import re
from .util import write_tweets

DEFAULT_INPUT_FILE = 'txt/mini_mostre.txt'
DEFAULT_OUTPUT_FILE = 'txt/extract.txt'
DEFAULT_FIELDS = ('TextTW', 'Lang')

def extract(fields, filename):
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
            tweet = tuple(fields_pattern.findall(tweet_info))
            if tweet:
                tweets.append(tweet)

    return tweets

if __name__ == "__main__":
    import argparse as ap

    parser = ap.ArgumentParser(description=extract.__doc__)
    parser.add_argument('fields', type=str, nargs='*',
                        default=DEFAULT_FIELDS,
                        help='fields to be extracted')
    parser.add_argument('infile', nargs='?', type=ap.FileType('r'),
                        default=DEFAULT_INPUT_FILE)
    parser.add_argument('outfile', nargs='?', type=ap.FileType('r'),
                        default=DEFAULT_OUTPUT_FILE)
    
    args = parser.parse_args()
    
    write_tweets(extract(args.fields, args.infile.name),
                 args.outfile.name)
