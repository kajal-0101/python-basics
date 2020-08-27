'''
Write a python program to find the word “Python” from the given text file and do the
following operations,
• Count the number of words in text file.
• Count the occurrences of word “Python”.
'''

fname = input("Enter file name: ")
wc = 0
oc = 0
with open(fname, 'r') as f:
    for l in f:
        w = l.split()
        wc += len(w)

print("No of words in the given file {} is {}".format(fname, wc))

word = input("Enter the word to be searched: ")
with open(fname, 'r') as g:
    for m in g:
        w1 = m.split()
        for i in w1:
            if(i == word):
                oc = oc + 1

print("The occurence of the word {} in the file {} is {}".format(word, fname, oc))
