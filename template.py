from .util import *

DEFAULT_INPUT_FILE = ''
DEFAULT_OUTPUT_FILE = ''
DEFAULT_OUTPUT_TXT_FILE = ''

@optional_input(DEFAULT_INPUT_FILE)
@optional_output(DEFAULT_OUTPUT_FILE, DEFAULT_OUTPUT_TXT_FILE)
def function(*args, **kwargs):
    """Doc"""
    pass

if __name__ == "__main__":
    import argparse as ap

    argparser = ap.ArgumentParser(description=function.__doc__)
    add_io_argparser(argparser, DEFAULT_INPUT_FILE, DEFAULT_OUTPUT_FILE,
                     DEFAULT_OUTPUT_TXT_FILE)
    args = argparser.parse_args()

    function(args.fields, args.in_file, output=args.out_file,
             txt=args.txt_file)
