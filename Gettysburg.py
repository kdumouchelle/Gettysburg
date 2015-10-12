__author__ = 'Kyle Dumouchelle'
#Midterm project, CPSC 409
import os
from string import punctuation
import collections

my_path = "./data"
address = ""
my_file = open(os.path.join(my_path, "text.txt"), "r")
for line in my_file.readlines():
    address = address + line

punct = set(punctuation)
address = address.replace("\n", " ")
address = ''.join(letter for letter in address if letter not in punct).lower()

words = address.split()
words.sort()
word_dict = collections.Counter()
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
print(word_dict.most_common(15))