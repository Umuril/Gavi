from googletrans import Translator

from .util import load_tweets, dump_tweets, add_io_argparser, write_tweets_txt
from . import extract

TEXT_FIELD = 'TextTW'
LANG_FIELD = 'Lang'
UNKNOWN_LANG = 'und'
LANG = 'en'
DEFAULT_OUTPUT_FILE = 'out/translated.pkl'
DEFAULT_OUTPUT_TXT_FILE = 'txt/translated.txt'

def translate(filename, lang):
    """Translates all the tweets to the same language"""
    translator = Translator()

    tweets = load_tweets(filename)
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
    add_io_argparser(argparser, extract.DEFAULT_OUTPUT_FILE,
                     DEFAULT_OUTPUT_FILE, DEFAULT_OUTPUT_TXT_FILE)
    args = argparser.parse_args()
    
    tweets = translate(args.in_file.name, args.lang)
    dump_tweets(tweets, args.out_file.name)
    if args.txt_file:
        write_tweets_txt(tweets, args.txt_file.name)
