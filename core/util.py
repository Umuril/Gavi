import pickle
import argparse as ap

def write_tweets_txt(tweets, filename):
    with open(filename, 'w') as out_file:
        for tweet in tweets:
            for field, content in tweet.items():
                out_file.write(field + ' : ' + content + '\n')
            out_file.write('\n')

def dump_tweets(tweets, filename):
    with open(filename, 'wb') as out_file:
        pickle.dump(tweets, out_file, pickle.HIGHEST_PROTOCOL)

def load_tweets(filename):
    with open(filename, 'rb') as in_file:
        return pickle.load(in_file)

def add_io_argparser(argparser, default_input, default_output,
                     default_output_txt):
    argparser.add_argument('-i', dest='in_file',
                           type=ap.FileType('r'), default=default_input)
    argparser.add_argument('-o', dest='out_file',
                           type=ap.FileType('w'), default=default_output)
    argparser.add_argument('-t', '--txt', dest='txt_file', nargs='?',
                           type=ap.FileType('w'), const=default_output_txt,
                           help='output in text mode to this file')
