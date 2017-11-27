from core import *

def main():
    tweets = extract.extract(txt = True)
    #duplicates()
    tweets = translate.translate(tweets = tweets, txt = True)

if __name__ == '__main__':
    main()
