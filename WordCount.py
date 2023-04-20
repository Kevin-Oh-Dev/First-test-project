from operator import itemgetter

word_counts = dict()
lines = open("d://WorkSpace//PythonStudy//WordCount//sample.txt")

for line in lines:
    line.lstrip()
    words = line.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

# sort by value
sorted_by_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse = True)
for key, value in sorted_by_counts[:10]:
    print(value, key)

