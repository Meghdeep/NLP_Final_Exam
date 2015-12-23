finalout  = open('final out.txt', 'w')
csvfile = open('outfile.txt', 'r')
for i in csvfile.readlines():
    if i == ",\n":
        continue
    else:
        finalout.write(i)
