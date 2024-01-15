def wordcount(str):
    counts=dict()
    words=str.split()
    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] =1
    return counts
print(wordcount("it is very very big is"))  

# This program is written in the Python programming language and it counts the frequency of each word in a given string. It does this in three steps:

# First, the program splits the input string "To change the overall look your document. To change the look available in the gallery" into a list of words "txt" using the built-in "split" method with a delimiter of " ".
# Next, the program creates an empty dictionary "c" to store the count of each word.
# The program then uses a for loop to iterate over each word in the list "txt". For each iteration, the program checks if the current word is already a key in the dictionary "c". If it is, then the value associated with that key is incremented by 1. If it is not, then a new key is created in the dictionary with the value set to 1.
# Finally, the program prints the dictionary "c", which contains the frequency of each word in the input string.
