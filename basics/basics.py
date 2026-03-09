from factors import get_prime_factors
from palindrome import is_palindrome
from str_sort import sort_words

if __name__ == "__main__":
    spacer = "-" * 20

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
    print(sort_words("banana APPLE cherry")) # Output: "apple banana cherry"
    print(sort_words("hello World")) # Output: "hello world"
    print(sort_words("Python programming language")) # Output: "language programming python"
