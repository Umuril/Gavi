import itertools

with open('txt/prove.txt') as filefrom, open('txt/prove2.txt', 'w') as fileto:
    for key, group in itertools.groupby(filefrom, lambda line: line == '\n'):
        if not key:
            tweet = {}
            for item in group:
                splitted = item.split(':')
                field, value = splitted[0].strip(), ':'.join(splitted[1:]).strip()
                tweet[field] = value

            # Codice qui
            if tweet["Text"].startswith("RT") and "Retweet-count" not in tweet.keys():
                pass
            else:
                tweet = {}

            for k, v in tweet.items():
                fileto.write(str(k) + " : " + str(v) + '\n')
            fileto.write('\n')
