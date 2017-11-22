
out_file = open("txt/prove.txt", "w")

s = ""
lasttext = ""

i = 0
with open('txt/mostre.txt') as f:
    for line in f:
        line = line.strip()
        if line.startswith("TextTW") or line.startswith("Lang") or line.startswith("Retweet-count"):
            if line.startswith("TextTW"):
                line = "Text" + line[6:]
            lasttext = line[6:]
            s += line + '\n'
            i += 1
        elif(len(line) == 0):
            if (i > 1):
                out_file.write(s + '\n')
                s = ""
                i = 0
        elif(len(line.split()) < 2 or line.split()[1] != ':'):
            s = s[:-1] + ' ' + line + '\n'

out_file.write(s)
out_file.close()