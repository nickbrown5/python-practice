
# saves python dictionary to a file
def save_dict(dictionary, filename):
    with open(filename, "w") as file:
        for key, value in dictionary.items():
            file.write(f"{key}:{value}\n")

# loads python dictionary from a file
def load_dict(filename):
    with open(filename, "r") as file:
        dictionary = {}
        for line in file:
            key, value = line.strip().split(":")
            dictionary[key] = value
    return dictionary

if __name__ == "__main__":
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    save_dict(my_dict, "my_dict.txt")
    loaded_dict = load_dict("my_dict.txt")
    print(loaded_dict)