import itertools
import string

def match():
    elementSet={}  #qua ci va l'elenco del set iniziale delle mostre con i corrispondenti eventi

    with open('txt/startedSet.txt') as startedfile:
        for line in startedfile:
            splitted = line.split(':')
            field, value = splitted[0].strip(), ':'.join(splitted[1:]).strip()
            elementSet[field] = value

    print(str(elementSet))

    with open('txt/translate.txt') as filefrom:    #file di partenza
        with open('txt/match.txt', 'w') as fileto:  #file di destinazione
            for key, group in itertools.groupby(filefrom, lambda line: line == '\n'):   #ciclo per prendere un tweet alla volta
                if not key:  #quando key=false significa che il ciclo è arrivato a leggere l'invio che separa i tweet
                    tweet = {}  #dictionary
                    for item in group: #ciclo per dividere la coppia chiave:valore per ogni tweet
                        splitted = item.split(':')
                        field, value = splitted[0].strip(), ':'.join(splitted[1:]).strip()
                        tweet[field] = value

    print(str(tweet))
                    # qui ho il dictionary tweet che contiene un solo tweet con i soli parametri che mi servono e tradotto in inglese
                    # Codice qui

    # lista delle parole del tweet in questione
    # for values in tweet.values():
    #     string= values
    #     wordlist= string.split()
    #     print(wordlist)

    #lista delle parole del set senza spazi
    for key, values in elementSet.items():
        stringKey= key.replace(' ', '')
        stringValues = values.replace(' ', '')
        print(stringKey)
        print(stringValues)

    #confronto con le parole del tweet e quella della lista    (string.find("banana", "na") restituisce 2)
    for word in wordlist:
        if (string.find(stringValues.upper(), word.upper()))!= 0: #se è diverso da zero significa che word è in stringValues
        #allora ho trovato il match in teoria quindi dovrei aggiungere il campo "nome mostra" al tweet
            pass





                    # for k, v in tweet.items():
                    #     fileto.write(str(k) + " : " + str(v) + '\n')
                    # fileto.write('\n')

if __name__ == '__main__':
    match()
