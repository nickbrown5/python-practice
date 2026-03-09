
# function to sort words in a string alphabetically
def sort_words(str):
    return ' '.join(sorted(str.split(), key=lambda w: w.lower()))
