# Regular expression library
import re

# Add or remove the words in this list to vary the results
wordlist = ["color", "colour", "work", "working",
            "fox", "worker", "working"]

for word in wordlist:
        # The . symbol is used in place of ? symbol
        if re.search('col.r', word) :
                print (word)