# import time
# import random
# import matplotlib.pyplot as plt

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)


# def measure_time(size_of_array, is_worst_case=False):
#     if is_worst_case:
#         array = list(range(size_of_array, 0, -1))  # Generate array in descending order
#     else:
#         array = [random.randint(1, size_of_array) for _ in range(size_of_array)]

#     with open('average_case_array.txt', 'a') as file:
#         file.seek(0, 2)
#         file.write(f'size of {size_of_array}: {array}\n\n')

#     start_time = time.time()
#     quicksort(array)
#     end_time = time.time()

#     return end_time - start_time


# input_size_start = 10
# input_size_end = 100000
# input_sizes = []

# while input_size_start <= input_size_end:
#     input_sizes.append(input_size_start)

#     if input_size_start < 100:
#         input_size_start += 10
#     elif input_size_start < 1000:
#         input_size_start += 100
#     elif input_size_start < 10000:
#         input_size_start += 1000
#     else:
#         input_size_start += 10000


# execution_times = []
# start_time_total = time.time()
# for size in input_sizes:
#     execution_time = measure_time(size)
#     execution_times.append(execution_time)
# end_time_total = time.time()

# total_execution_time = end_time_total - start_time_total


# # Write execution_times to a text file
# with open('execution_times.txt', 'w') as file:
#     for time_val, sizes in zip(execution_times, input_sizes):
#         file.write(f'{sizes} = {time_val:.16f}\n')

# # To measure the worst-case time complexity
# worst_execution_times = []
# for size in input_sizes:
#     execution_time = measure_time(size, is_worst_case=True)
#     worst_execution_times.append(execution_time)

# # Write worst_execution_times to a text file
# with open('worst_case_execution_times.txt', 'w') as file:
#     for time_val, sizes in zip(worst_execution_times, input_sizes):
#         file.write(f'{sizes} = {time_val:.16f}\n')

# worst_total_execution_time = sum(worst_execution_times)



# # Plot the results for worst-case time complexity
# plt.plot(input_sizes, worst_execution_times, marker='.')
# plt.xlabel('Input Size')
# plt.ylabel('Execution Time (seconds)')
# plt.title(f'Quick Sort Time Complexity (Worst Case)\nTotal Execution Time: {worst_total_execution_time:.2f}')
# plt.grid(True)
# plt.show()



import matplotlib.pyplot as plt
import time
import random

def quicksort_worst_case(arr, low, high):
    if low < high:
        pivot = find_pivot(arr, low, high)
        quicksort_worst_case(arr, low, pivot-1)
        quicksort_worst_case(arr, pivot+1, high)

def find_pivot(arr, low, high):
    # Choosing a random pivot from the subarray
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    return pivot_index

def analyze_time_complexity():
    n_values = []  # Array to store the number of elements
    time_complexity = []  # Array to store the corresponding time complexity values

    step = 10000
    iterations = 50
    for i in range(iterations):
        n = (i + 1) * step
        arr = random.sample(range(1, n+1), n)  # Generate a random array of size n

        # Measure the time taken for sorting
        start_time = time.time()
        quicksort_worst_case(arr, 0, len(arr)-1)
        end_time = time.time()
        execution_time = end_time - start_time

        # Append values to the arrays
        n_values.append(n)
        time_complexity.append(execution_time)

    # Plot the graph
    plt.plot(n_values, time_complexity, marker=".")
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time Complexity (seconds)')
    plt.title('Quick Sort - Worst Case Time Complexity')
    plt.show()

# Run the analysis
analyze_time_complexity()
