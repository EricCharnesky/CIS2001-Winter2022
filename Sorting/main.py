# selection sort

# best case ( n^2 )
# average(n^2)
# worst (n^2)

# find the smallest item, move to the front
def selection_sort(some_list):

    for current_index in range(len(some_list) - 1):
        smallest_item_index = current_index
        for index in range(current_index, len(some_list)):
            if some_list[index] < some_list[smallest_item_index]:
                smallest_item_index = index
        temp = some_list[current_index]
        some_list[current_index] = some_list[smallest_item_index]
        some_list[smallest_item_index] = temp

# insertion sort
# best case - already sorted O(n)
# worst case - O(n^2)
# average - O(n^2)
def insertion_sort(some_list):
    for index_to_sort in range(1, len(some_list)):
        current_index = index_to_sort
        while current_index > 0 and some_list[current_index] < some_list[current_index - 1]:
            temp = some_list[current_index]
            some_list[current_index] = some_list[current_index -1]
            some_list[current_index - 1] = temp
            current_index -= 1

# priority queue ( heap sort ) O ( n log n )
# binary search tree O ( n log n )


values = [ 4, 2, 99, 7, 30, 12, 15]
print(values)
insertion_sort(values)
print(values)