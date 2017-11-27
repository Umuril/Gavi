import pickle
import os

def write_tweets(tweets, filename):
    with open(filename, 'w') as out_file:
        for tweet in tweets:
            for field, content in tweet.items():
                out_file.write(field + ' : ' + content + '\n')
            out_file.write('\n')

def dump_tweets(tweets, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as out_file:
        pickle.dump(tweets, out_file, pickle.HIGHEST_PROTOCOL)

def load_tweets(filename):
    with open(filename, 'rb') as in_file:
        return pickle.load(in_file)

class optional_input:
    def __init__(self, default_input_file):
        self.default_input_file = default_input_file

    def __call__(self, function):
        def decorator(*args, **kwargs):
            input_file = kwargs.pop('input_file', None)

            if input_file is not None:
                args = (load_tweets(self.default_input_file
                                    if input_file is True else input_file),) \
                        + args[1:]

            return function(*args, **kwargs)
        return decorator

class optional_output:
    def __init__(self, default_output_file, default_output_txt_file):
        self.default_output_file = default_output_file
        self.default_output_txt_file = default_output_txt_file

    def __call__(self, function):
        def decorator(*args, **kwargs):
            output = kwargs.pop('output', None)
            txt = kwargs.pop('txt', None)
            tweets = function(*args, **kwargs)

            for param, default_file, out_func in zip(
                (output, txt),
                (self.default_output_file, self.default_output_txt_file),
                (dump_tweets, write_tweets)):
                if param is not None:
                    out_func(tweets,
                             default_file if param is True else param)
            
            return tweets
        return decorator

def add_io_argparser(argparser, default_input, default_output,
                     default_output_txt):
    argparser.add_argument('-i', dest='in_file', default=default_input)
    argparser.add_argument('-o', dest='out_file', default=default_output)
    argparser.add_argument('-t', '--txt', dest='txt_file', nargs='?',
                           const=default_output_txt,
                           help='output in text mode to this file')
