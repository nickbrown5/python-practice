
# function to sort words in a string alphabetically
def sort_words(str):
    sorted_words = ' '.join(sorted(str.split(), key=lambda w: w.lower()))
    return sorted_words
