words = {}

with open('words.txt') as f:
    for line in f:
        for word in line.split():
            if word in words:
                words[word]+=1
            else:
                words[word] = 1
print(words)
    

