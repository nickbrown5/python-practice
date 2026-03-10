
# Return a list of all indices where value occurs in the list.
def index_all(inList, value):
    indices = []
    for index, item in enumerate(inList):
        if item == value:
            indices.append([index])
        elif isinstance(inList[index], list):
            for sub_index in index_all(inList[index], value):
                indices.append([index] + sub_index)

    return indices