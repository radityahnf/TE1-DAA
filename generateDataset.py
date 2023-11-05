from random import randint
def generate_datasets():
    small_random_dataset = [randint(0, 20000) for _ in range(200)]
    medium_random_dataset = [randint(0, 20000) for _ in range(2000)]
    big_random_dataset = [randint(0, 20000) for _ in range(20000)]

    small_sorted_dataset = sorted(small_random_dataset)
    medium_sorted_dataset = sorted(medium_random_dataset)
    big_sorted_dataset = sorted(big_random_dataset)

    small_reversed_dataset = small_sorted_dataset[::-1]
    medium_reversed_dataset = medium_sorted_dataset[::-1]
    big_reversed_dataset = big_sorted_dataset[::-1]

    return small_random_dataset, medium_random_dataset, big_random_dataset, \
           small_sorted_dataset, medium_sorted_dataset, big_sorted_dataset, \
           small_reversed_dataset, medium_reversed_dataset, big_reversed_dataset
           
           
def export_dataset_to_file(dataset, filename):
    with open(filename, 'w') as file:
        for item in dataset:
            file.write(str(item) + '\n')

# Generate the datasets
small_random_dataset, medium_random_dataset, big_random_dataset, \
small_sorted_dataset, medium_sorted_dataset, big_sorted_dataset, \
small_reversed_dataset, medium_reversed_dataset, big_reversed_dataset = generate_datasets()

# Export each dataset to a separate file
export_dataset_to_file(small_random_dataset, "small_random_dataset.txt")
export_dataset_to_file(small_sorted_dataset, "small_sorted_dataset.txt")
export_dataset_to_file(small_reversed_dataset, "small_reversed_dataset.txt")
export_dataset_to_file(medium_random_dataset, "medium_random_dataset.txt")
export_dataset_to_file(medium_sorted_dataset, "medium_sorted_dataset.txt")
export_dataset_to_file(medium_reversed_dataset, "medium_reversed_dataset.txt")
export_dataset_to_file(big_random_dataset, "big_random_dataset.txt")
export_dataset_to_file(big_sorted_dataset, "big_sorted_dataset.txt")
export_dataset_to_file(big_reversed_dataset, "big_reversed_dataset.txt")
