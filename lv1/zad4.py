dictionary={}
file=open('lv1\song.txt')
for line in file:
    for word in line.split():
        if word not in dictionary:
            dictionary[word] = 1
    for word in line.split():
        if word in dictionary:
            dictionary[word] += 1

print(dictionary)