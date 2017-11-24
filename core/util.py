def write_tweets(tweets, filename):
    with open(filename, 'w') as out_file:
        for tweet in tweets:
            for key, value in tweet.items():
                out_file.write(key + ' : ' + value + '\n')
            out_file.write('\n')

