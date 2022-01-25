def count_down(nth):
    print(nth)
    if nth > 0:
        count_down(nth-1)

def count_down_loop(nth):
    for value in range(nth, 0, -1):
        print(value)

def _binary_search(some_list, number_to_find, start_index, end_index):
    if start_index > end_index:
        raise ValueError(number_to_find + " is not in the list")
    mid = (start_index + end_index) // 2 # truncate or round down
    if some_list[mid] == number_to_find:
        return mid
    if some_list[mid] < number_to_find:
        return _binary_search(some_list, number_to_find, mid+1, end_index)
    return _binary_search(some_list, number_to_find, start_index, mid-1)

# only works on sorted lists
def binary_search(some_list, number_to_find):
    return _binary_search(some_list, number_to_find, 0, len(numbers)-1)

def iterative_binary_search(some_list, number_to_find):
    start_index = 0
    end_index = len(some_list) - 1
    while start_index < end_index:
        mid = (start_index + end_index) // 2  # truncate or round down
        if some_list[mid] == number_to_find:
            return mid
        if some_list[mid] < number_to_find:
            start = mid+1
        else:
            end = mid-1


numbers = [ 18, 22, 28, 46, 94, 108, 607, 2004, 2, 0]

sorted_copy_of_numbers = sorted(numbers)# generates a new list

numbers.sort() # modifies the list being called on


for value in numbers:
    print("the index of {} in the list is: {}".format(
        value, binary_search(numbers, value)))
