file = open("day_1_input", "r")
measurements_str_list = file.read().splitlines()
file.close()

# How many measurements are larger than the previous measurement?
# iterate thru the list
# compare i'th item to its ith - 1 if exists
# increment some counter for increased measurements
# return counter

def count_measurements_increased(str_list) -> int:
    increased_count = 0
    for index, measurement in enumerate(str_list):
        if index == 0:
            pass
        else:
            if int(measurement) > int(str_list[index - 1]):
                increased_count += 1

    return increased_count


print(count_measurements_increased(measurements_str_list))

# Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
# Create a previous_window_lookback sum that starts as None
# Create the lookback sum of the past 2 + ith measurement
# Compare this to previous lookback to increment counter
# Set current sum to previous_window_lookback before incrementing in loop

def count_sliding_sum_increased(str_list) -> int:
    increased_count = 0
    previous_window_lookback = None

    for index, measurement in enumerate(str_list):
        if index == 0 or index == 1:
            pass 
        current_window_sum = int(measurement) + int(str_list[index - 1]) + int(str_list[index - 2])
        if previous_window_lookback and current_window_sum > previous_window_lookback:
            increased_count += 1
        previous_window_lookback = current_window_sum

    return increased_count


print(count_sliding_sum_increased(measurements_str_list))