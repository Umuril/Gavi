import itertools
from googletrans import Translator

def translate():
    translator = Translator()

    with open('txt/duplicates.txt') as filefrom:
        with open('txt/translate.txt', 'w') as fileto:
            for key, group in itertools.groupby(filefrom, lambda line: line == '\n'):
                if not key:
                    tweet = {}
                    for item in group:
                        splitted = item.split(':')
                        field, value = splitted[0].strip(), ':'.join(splitted[1:]).strip()
                        tweet[field] = value

                    if (tweet["Lang"] != 'en'):
                        if (tweet["Lang"] == 'und'):
                            tweet["Text"] = translator.translate(tweet["Text"]).text
                        else:
                            tweet["Text"] = translator.translate(tweet["Text"], src=tweet["Lang"]).text



                    for k, v in tweet.items():
                        fileto.write(str(k) + " : " + str(v) + '\n')
                    fileto.write('\n')

if __name__ == '__main__':
    translate()