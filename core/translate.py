from googletrans import Translator

from .util import *
from . import extract

TEXT_FIELD = 'TextTW'
LANG_FIELD = 'Lang'
UNKNOWN_LANG = 'und'
LANG = 'en'
DEFAULT_INPUT_FILE = extract.DEFAULT_OUTPUT_FILE
DEFAULT_OUTPUT_FILE = 'out/translated.pkl'
DEFAULT_OUTPUT_TXT_FILE = 'txt/translated.txt'

@optional_input(DEFAULT_INPUT_FILE)
@optional_output(DEFAULT_OUTPUT_FILE, DEFAULT_OUTPUT_TXT_FILE)
def translate(tweets, lang=LANG):
    """Translates all the tweets to the same language"""
    translator = Translator()

    for tweet in tweets:
        if tweet[LANG_FIELD] == UNKNOWN_LANG:
            tweet[LANG_FIELD] = 'auto'

        if tweet[LANG_FIELD] != LANG:
            tweet[TEXT_FIELD] = translator.translate(tweet[TEXT_FIELD],
                                                     src=tweet[LANG_FIELD],
                                                     dest=lang).text

    return tweets

if __name__ == '__main__':
    import argparse as ap

    argparser = ap.ArgumentParser(description=translate.__doc__)
    argparser.add_argument('-l', '--lang', default=LANG,
                           help='destination language')
    add_io_argparser(argparser, DEFAULT_INPUT_FILE, DEFAULT_OUTPUT_FILE,
                     DEFAULT_OUTPUT_TXT_FILE)
    args = argparser.parse_args()
    
    translate(args.in_file, args.lang)
