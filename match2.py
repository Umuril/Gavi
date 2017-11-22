import itertools
import re

def match2():
    regex = re.compile(r'\W')

    elementSet = {}  #qua ci va l'elenco del set iniziale delle mostre con i corrispondenti eventi

    with open('txt/startedSet.txt') as startedfile:
        for line in startedfile:
            splitted = line.split(':')
            field = splitted[0].strip()
            value = ' '.join([x.strip() for x in splitted]).strip()
            elementSet[field] = value

    with open('txt/translate.txt') as filefrom, open('txt/match.txt', 'w') as fileto:
        for key, group in itertools.groupby(filefrom, lambda line: line == '\n'):
            if not key:
                tweet = {}
                for item in group:
                    splitted = item.split(':')
                    field, value = splitted[0].strip(), ':'.join(splitted[1:]).strip()
                    tweet[field] = value

                tweet["Mostra"] = "Sconosciuta"

                # Codice qui
                for word in tweet["Text"].split():
                    word = regex.sub('', word.lower())
                    for k, v in elementSet.items():
                        v = v.lower().replace(':','').split(' ')
                        # word = word.replace('#','').lower().replace('@','').replace(':','')
                        print(k, v, word)
                        if word in v:
                            print("QUI")
                            tweet["Mostra"] = k
                            break

                for k, v in tweet.items():
                    fileto.write(str(k) + " : " + str(v) + '\n')
                fileto.write('\n')
                
if __name__ == '__main__':
    match2()