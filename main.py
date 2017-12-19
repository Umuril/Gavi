from core import *

def main():
##    tweets = extract.extract(txt=True)
##    duplicates()
##    tweets = translate.translate(tweets)
    tweets = utils.load_tweets('out/no_duplicates')
    for i in range(0, len(tweets)-1000, 1000):
        utils.dump_tweets(tweets[i:i+1000], 'out/'+str(i)+'-'+str(i+999))
    utils.dump_tweets(tweets[i+1000:],
                      'out/'+str(i+1000)+'-'+str(len(tweets)))
    
if __name__ == '__main__':
    main()

