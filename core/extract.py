import re
from util import write_tweets

fields = ('TextTW', 'Lang') # fields to be extracted

# Pattern used to split the file in single tweet's block of information.
# A block is identified by two newline characters followed by a field
# name or by the end of the string.
split_pattern = re.compile(r'\n\n(?=[A-z_-]+ : |\Z)')
# Pattern used to extract only some fields. It matches both the field
# name and the content. The content matches every character that is not
# the next field or the end of the string.
fields_pattern = re.compile(r'(^' +
                            '|'.join(fields) +
                            ') : (.+?)(?=\n+[A-z_-]+ : |\Z)',
                            re.MULTILINE | re.DOTALL)

def extract():
    """Extracts only valuable fields from the tweets"""
    tweets = []

    with open('../txt/mini_mostre.txt') as in_file:
        for tweet_info in split_pattern.split(in_file.read()):
            tweet = dict(fields_pattern.findall(tweet_info))
            if tweet:
                tweets.append(tweet)

    write_tweets(tweets, '../txt/extract.txt')

##    tweets = []
##    
##    with open('../txt/mini_mostre.txt') as in_file:
##        tweet = {}
##        for line in in_file:
##
##            if line.startswith(fields):
##                pass
##
##            for field in renamed_fields:
##                if line.startswith(field):
##                    tweet[renamed_fields[field]] = line[len(field):].strip('\n :')
##                    break
##
##            if line.startswith(fields):
##                tweet.update([[x.strip() for x in line.split(':', 1)]])
##
##            if not line.strip() and tweet:
##                tweets.append(tweet)
##                tweet = {}
##
##    with open("../txt/extract.txt", "w") as out_file:
##        for i in tweets:
##            out_file.write(str(i)+'\n')

if __name__ == "__main__":
    extract()
