def linear_search(value_to_find, array_to_search_through):
    for index in range(len(array_to_search_through)):
        if array_to_search_through[index] == value_to_find:
            return index
    return None

def linear_search_global(value_to_find, array_to_search_through):
    indices = []
    for index in range(len(array_to_search_through)):
        if array_to_search_through[index] == value_to_find:
            indices.append(index)
    return indices