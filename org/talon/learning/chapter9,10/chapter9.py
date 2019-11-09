#1 Mystery Code. a=20, b=0

#2 A Hidden Message

sentance = "this if is you not are a reading very this good then way you to have hide done a it message wrong"
words=sentance.split()
for x in range(0, len(words), 2):
    print(words[x])

#3 Copying A Fild

f = open('test.txt')
s = f.read()
f.close()
f = open('output.txt', 'w')
f.write(s)
f.close()

