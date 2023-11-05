from random import randint, randrange
import time
import tracemalloc
   
def binary_loc_finder(arr, start, end, key):
    if start == end:
        if arr[start] > key:
            loc = start
            return loc
        else:
            loc = start + 1
            return loc
    if start > end:
        loc = start
        return loc
    else:
        middle = (start + end) // 2
        if arr[middle] < key:
            return binary_loc_finder(arr, middle + 1, end, key)
        elif arr[middle] > key:
            return binary_loc_finder(arr, start, middle - 1, key)
        else:
            return middle

def place_inserter(arr, start, end):
    temp = arr[end]
    for k in range(end, start, -1):
        arr[k] = arr[k - 1]
    arr[start] = temp
    return arr

def clustered_binary_insertion_sort(arr):
    POP = 0
    for i in range(1, len(arr)):
        COP = i
        key = arr[COP]
        if key >= arr[POP]:
            place = binary_loc_finder(arr, POP + 1, COP - 1, key)
        else:
            place = binary_loc_finder(arr, 0, POP - 1, key)
        POP = place
        arr = place_inserter(arr, place, COP)
    return arr




#Quicksort with Lomuto Partition	
def quicksort(arr, start, end):
	if start < end:
		index_pivot = partitionrand(arr, start, end)
		quicksort(arr, start, index_pivot-1)
		quicksort(arr, index_pivot+1, end)
	
	return arr


def partitionrand(arr , start, stop):
	randpivot = randrange(start, stop)
	arr[start], arr[randpivot] = \
		arr[randpivot], arr[start]
	return partition(arr, start, stop)


def partition(arr,start,stop):
	pivot = start 
	
	i = start + 1
	
	for j in range(start + 1, stop + 1):
		
		if arr[j] <= arr[pivot]:
			arr[i] , arr[j] = arr[j] , arr[i]
			i = i + 1
	arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
	pivot = i - 1
	return (pivot)

def run_algorithm(alg, arr, arr_type):
    
    start = time.time()
    tracemalloc.start()
    if alg == "CBIS":
        print(f"Running CBIS for: {arr_type}")
        clustered_binary_insertion_sort(arr)
    elif alg == "QS":
        print(f"Running QS for: {arr_type}")
        quicksort(arr, 0, len(arr)-1)
        
    end = time.time()
    _, peak = tracemalloc.get_traced_memory()
    print(f"Traced Memory {peak}")
    tracemalloc.stop()
    print(f"Finished execution. Time: {(end-start) * 10**3} ms\n")
    
def read_dataset_from_file(filename):
    dataset = []
    with open(filename, 'r') as file:
        for line in file:
            dataset.append(int(line.strip()))
    return dataset




if __name__ == "__main__":
    small_random_dataset = read_dataset_from_file("small_random_dataset.txt")
    small_sorted_dataset = read_dataset_from_file("small_sorted_dataset.txt")
    small_reversed_dataset = read_dataset_from_file("small_reversed_dataset.txt")
    medium_random_dataset = read_dataset_from_file("medium_random_dataset.txt")
    medium_sorted_dataset = read_dataset_from_file("medium_sorted_dataset.txt")
    medium_reversed_dataset = read_dataset_from_file("medium_reversed_dataset.txt")
    big_random_dataset = read_dataset_from_file("big_random_dataset.txt")
    big_sorted_dataset = read_dataset_from_file("big_sorted_dataset.txt")
    big_reversed_dataset = read_dataset_from_file("big_reversed_dataset.txt")

    run_algorithm("CBIS", small_random_dataset, "small_random_dataset")
    run_algorithm("QS", small_random_dataset, "small_random_dataset")
    run_algorithm("CBIS", small_sorted_dataset, "small_sorted_dataset")
    run_algorithm("QS", small_sorted_dataset, "small_sorted_dataset")
    run_algorithm("CBIS", small_reversed_dataset, "small_reversed_dataset")
    run_algorithm("QS", small_reversed_dataset, "small_reversed_dataset")
    run_algorithm("CBIS", medium_random_dataset, "medium_random_dataset")
    run_algorithm("QS", medium_random_dataset, "medium_random_dataset")
    run_algorithm("CBIS", medium_sorted_dataset, "medium_sorted_dataset")
    run_algorithm("QS", medium_sorted_dataset, "medium_sorted_dataset")
    run_algorithm("CBIS", medium_reversed_dataset, "medium_reversed_dataset")
    run_algorithm("QS", medium_reversed_dataset, "medium_reversed_dataset")
    run_algorithm("CBIS", big_random_dataset, "big_random_dataset")
    run_algorithm("QS", big_random_dataset, "big_random_dataset")
    run_algorithm("CBIS", big_sorted_dataset, "big_sorted_dataset")
    run_algorithm("QS", big_sorted_dataset, "big_sorted_dataset")
    run_algorithm("CBIS", big_reversed_dataset, "big_reversed_dataset")
    run_algorithm("QS", big_reversed_dataset, "big_reversed_dataset")