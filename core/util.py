def write_tweets(tweets, filename):
    with open(filename, 'w') as out_file:
        for tweet in tweets:
            for field, content in tweet:
                out_file.write(field + ' : ' + content + '\n')
            out_file.write('\n')

