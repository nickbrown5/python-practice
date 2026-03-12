import re
import collections

# function to count number of unique words in text file
def count_unique_words(textfile):
    with open(textfile, "r", encoding="utf-8") as file:
        words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        words = [word.upper() for word in words]
        print(f'Total Words: {len(words)}')

        word_counts = collections.Counter(words)
        print('Top 20 most frequent words:')
        for word in word_counts.most_common(20):
            print(f'{word[0]}\t{word[1]}')

if __name__ == '__main__':
    print('\nThe Complete Works of William Shakespeare')
    count_unique_words('will.txt')
    print('\nLorem Ipsum Text')
    count_unique_words('lorem.txt')