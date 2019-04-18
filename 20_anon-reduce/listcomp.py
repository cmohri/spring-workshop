# to the lighthouse: Clara Mohri & Michelle Tang
# SoftDev pd6
# K #20: wee
# 2019-04-17

from functools import reduce

# read file
def open_file(file):
    file = open(file, "r")
    text = file.read().split()
    file.close()
    return text

# remove punctuation and make all lower case
def strip(text):
    return [x.strip(".?!;,-").lower() for x in text]

# Find the frequency of a single word
def single_freq(word, text):
    word = word.lower()
    list = [1 for x in text if x == word]
    if not len(list):
        return 0
    return reduce((lambda x, y: x+y), list)

# Find the total frequency of a group of words
def mult_freq(words, text):
    words = strip(words)
    l = len(words)
    sublists = ([text[index : index + l] for index in range(len(text)-l + 1)])
    # print(sublists)
    count = [1 for x in sublists if x == words]
    if not len(count):
        return 0
    return reduce((lambda x, y: x + y), count)

# Find the most frequently occurring word
def most_freq(text):
    s = set(text)
    freq = [{text.count(x): x} for x in s]
    vals = [list(x.keys())[0] for x in freq]
    m = max(vals)
    for i in freq:
        if m in i:
            return i[m]


# ["hi","there"]
text = open_file("hamlet.txt")
text = strip(text)
print(single_freq("there", text))
print(single_freq("i", text))

print(mult_freq(["to", "be", "or", "not"], text))
print(mult_freq(["hii", "three"], text))
print(most_freq(text))
