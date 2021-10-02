def find_max(array, max, current_index = 1):
    if current_index == len(array) - 1:
        return max

    if array[current_index] > max:
        return find_max(array, array[current_index], current_index + 1, )
    else:
        return find_max(array, max, current_index + 1)
