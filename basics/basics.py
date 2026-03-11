from factors import get_prime_factors
from palindrome import is_palindrome
from str_sort import sort_words
from index_all import index_all

if __name__ == "__main__":
    spacer = "-" * 30

    print("Prime factors:")
    print(get_prime_factors(630)) # Output: [2, 3, 3, 5, 7]
    print(get_prime_factors(28))  # Output: [2, 2, 7]
    print(get_prime_factors(17))  # Output: [17]

    print(spacer)
    print("Palindrome check:")
    print(is_palindrome("A man a plan a canal Panama")) # Output: True
    print(is_palindrome("Hello World")) # Output: False
    print(is_palindrome("Go hang a salami - I'm a lasagna hog")) # Output: True

    print(spacer)
    print("Sorted words:")
    print(sort_words("banana APPLE cherry")) # Output: "APPLE banana cherry"
    print(sort_words("hello World")) # Output: "hello World"
    print(sort_words("Python programming language")) # Output: "language programming Python"

    print(spacer)
    print("Index all occurrences:")
    print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2)) # Output: [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], [1, 2, 3])) # Output: [[0, 0], [1]]
    print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 4)) # Output: []