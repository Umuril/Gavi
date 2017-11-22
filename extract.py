def extract():
    out_file = open("txt/extract.txt", "w")

    s = ""

    i = 0
    with open('txt/mini_mostre.txt') as f:
        for line in f:
            line = line.strip()
            if line.startswith("TextTW"):
                line = "Text" + line[6:]
            if line.startswith("Retweet-count"):
                line = "Retweet" + line[13:]
            if line.startswith("TextTW") or line.startswith("Lang") or line.startswith("Retweet-count"):
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

if __name__ == "__main__":
    extract()