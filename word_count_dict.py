sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

word_counts = {}
for x in sentence.split():
    word_counts[x] = word_counts.get(x, 0) + 1