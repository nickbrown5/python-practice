
# function to sort words in a string alphabetically
def sort_words(str):
    words = str.split()
    sorted_words = sorted(words, key=lambda w: w.lower())
    return ' '.join(sorted_words)
