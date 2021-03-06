import re
import itertools as it
from googletrans import Translator

from .utils import *
from . import remove_duplicates, fields

DEFAULT_INPUT_FILE = remove_duplicates.DEFAULT_OUTPUT_FILE
DEFAULT_OUTPUT_FILE = 'out/translated'
DEFAULT_OUTPUT_TXT_FILE = 'out/translated.txt'
UNKNOWN_LANG = 'und'
DEFAULT_LANG = 'en'

@optional_input(DEFAULT_INPUT_FILE)
@optional_output(DEFAULT_OUTPUT_FILE, DEFAULT_OUTPUT_TXT_FILE)
def translate(tweets, lang=DEFAULT_LANG):
    """Translates all the tweets to the same language"""

    translator = Translator()

    # matches every character c that chr(c) <= 65535
    ignore_unicode_pattern = re.compile('[^\u0000-\uFFFF]')
    
    for tweet in tweets:
        if tweet[fields.LANG] == UNKNOWN_LANG:
            tweet[fields.LANG] = 'auto'

        if tweet[fields.LANG] != lang:
            text = ignore_unicode_pattern.sub('', tweet[fields.TEXT])
            try:
                tweet[fields.TEXT] = translator.translate(text,
                                                      src=tweet[fields.LANG],
                                                      dest=lang).text
            except Exception as e:
                print(e, tweet)

    return tweets

if __name__ == '__main__':
    import argparse as ap

    argparser = ap.ArgumentParser(description=translate.__doc__)
    argparser.add_argument('-l', '--lang', default=DEFAULT_LANG,
                           help='destination language')
    add_io_argparser(argparser, DEFAULT_INPUT_FILE, DEFAULT_OUTPUT_FILE,
                     DEFAULT_OUTPUT_TXT_FILE)
    args = argparser.parse_args()
    
    translate(args.lang, input_file=args.input_file,
              output_file=args.output_file,
              txt_file=args.txt_file)
