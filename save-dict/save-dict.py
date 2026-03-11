import pickle

# saves python dictionary to a file
def save_dict(dictionary, filename):
    with open(filename, "wb") as file:
        # first attempt
        # for key, value in dictionary.items():
        #     file.write(f"{key}:{value}\n")
        pickle.dump(dictionary, file)

# loads python dictionary from a file
def load_dict(filename):
    with open(filename, "rb") as file:
        # first attempt
    #     dictionary = {}
    #     for line in file:
    #         key, value = line.strip().split(":")
    #         dictionary[key] = value
    # return dictionary
        return pickle.load(file)

if __name__ == "__main__":
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    save_dict(my_dict, "my_dict.pickle")
    loaded_dict = load_dict("my_dict.pickle")
    print(loaded_dict)