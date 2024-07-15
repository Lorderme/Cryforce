# The code creates a web driver that checks which mnemonic phrases are valid 
# and collects them into a separate text file for further use.

import random

# Open the file with the list of words
with open('bip39.txt', 'r') as f:
    wordlist = [line.strip() for line in f]

# Set the length of the mnemonic phrase in words
mnemonic_length = 12

# Create an empty list to store unique mnemonic phrases
mnemonic_list = []

# Generate random mnemonic phrases
# The number specified should be changed depending on the number of phrases that need to be generated.
while len(mnemonic_list) < 50:
    mnemonic = ' '.join(random.sample(wordlist, mnemonic_length))
    if mnemonic not in mnemonic_list:
        mnemonic_list.append(mnemonic)

# Write the unique mnemonic phrases to a file
with open('Seed_phrases.txt', 'w') as f:
    for mnemonic in mnemonic_list:
        f.write(mnemonic + '\n')