from core import *

def main():
    tweets = extract.extract(output=True)
    #duplicates()
    tweets = translate.translate(txt=True, input_file=True)

if __name__ == '__main__':
    main()
