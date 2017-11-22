import itertools

def duplicates():
    tweets = []
    with open('txt/extract.txt') as f:
        for key, group in itertools.groupby(f, lambda line: line == '\n'):
            if not key:
                tweet = {}
                for item in group:
                    splitted = item.split(':')
                    field, value = splitted[0].strip(), ':'.join(splitted[1:]).strip()
                    tweet[field] = value
                if(any(tweet["Text"] == t["Text"] for t in tweets)):
                    tweets[[t["Text"] for t in tweets].index(tweet["Text"])]["DuplicatesCount"] += 1
                    tweets[[t["Text"] for t in tweets].index(tweet["Text"])]["DuplicatesCount"] += 1
                    pass
                else:
                    tweet["DuplicatesCount"] = 1
                    tweets.append(tweet)

    with open('txt/duplicates.txt', 'w') as f:
        for t in tweets:
            for k, v in t.items():
                f.write(str(k) + " : " + str(v) + '\n')
            f.write('\n')