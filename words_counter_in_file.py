import string
import sys

words = {}
sline = string.whitespace + string.punctuation + string.digits + "\"'"
filename = sys.argv[1]
print "Checking symbols:\n=============\n%s\n=============\n" % sline

for line in open(filename):
    for word in line.lower().split():
        word = word.strip(sline)
        words[word] = words.get(word, 0) + 1

for word in sorted(words):
    print("'{0}' occurs {1} times".format(word, words[word]))
