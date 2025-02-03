'''
This script is used to compute all descriptive statistics from a file
1. Reads the file (ex: TC1.txt, TC2.txt, etc..)
2. Computes all descriptive statistics
3. Performs time elasped and time calculation 
4. Prints outputs to ConvertionResults.txt amd console
'''

import sys
import time
import math

# Read File
def read_file(file_name):
    """
    Reads a file that contains a list of items.
    If the file contains any invalid values, it will print out an warning. 
    """
    numbers = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Warning: Invalid Number Found in the File: {line.strip()}")
    return numbers


# Descriptive Statistics
# Compute Mean
def calculate_mean(numbers):
    '''
    When calculating the mean we initially sum up all numbers in the file.
    Afterwards divide the toal sum by the total count of numbers.
    '''
    total_sum = 0 #Initialize total_sum
    for num in numbers:
        total_sum += num  #Add all the numbers in the file
    return total_sum / len(numbers) if numbers else 0

#Sort Numbers using Bubble Sort
def sort_numbers(numbers):
    '''
    This function will sort the numbers in the list in order to help determine the median
    '''
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap the elements
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Compute Median
def calculate_median(numbers):
    '''
    When calculating the median, we will first sort the numbers. 
    If the value is even then we retrieve teh average of the middle numbers.
    If the value is odd then we retrieve middle value.
    '''
    sort_numbers(numbers)
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    return numbers[len(numbers) // 2]


# Compute Mode
def calculate_mode(numbers):
    '''
    When calculating the mode we want to monitor the frequency of each number.
    The frequency takes into account how many times a number appears in the list.
    '''
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_count = max(frequency.values())
    mode_output = [key for key, value in frequency.items() if value == max_count]
    return max(mode_output)

#  Compute Variance
def calculate_variance(numbers, mean_output):
    '''
    In order to calculate the variance, subtract each number in the file with the 
    mean value and square the difference. 
    After squaring the difference, then all the values are added up.
    Lastly, after calculating the total sum of total_variance, 
    divide the sum by the total count of numbers. 
    '''
    total_variance = 0 #Initialize total_variance
    for num in numbers:
        total_variance += (num - mean_output) ** 2
    return total_variance / len(numbers)

# Compute Standard Deviation
def calculate_standard_deviation(variance_output):
    '''
    In order to calculate standard deviation just take the
    square root of the variance value.
    '''
    return math.sqrt(variance_output)


# Printing Results
def print_results(results,elapsed_time,calculation_time,file_name):
    '''
    Print results in console and output file StatisticsResults.txt.
    '''
    count_output,mean_output, median_output, mode_output, variance_output, std_output = results

    result_output = (
        f"FILE NAME: {file_name}\n"
        f"COUNT: {count_output}\n"
        f"MEAN: {mean_output}\n"
        f"MEDIAN: {median_output}\n"
        f"MODE: {mode_output}\n"
        f"VARIANCE: {variance_output}\n"
        f"STANDARD DEVIATION: {std_output}\n"
        f"TIME ELAPSED FOR EXECUTION: {elapsed_time:.6f} seconds\n"
        f"TIME FOR DATA CALCULATION: {calculation_time:.6f} seconds\n"
    )

    print(result_output) # Print to console

    # Write to file
    with open("StatisticsResults_"+file_name, 'w', encoding='utf-8') as file:
        file.write(result_output)

#Main Function
def main():
    '''
    The main function will execute all the functions. 
    THe elasped time and calcaultion time is calculated within this function.
    '''
    # Start time measurement
    start_time = time.time()

    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py <fileWithData.txt>")
        sys.exit(1)

    file_name = sys.argv[1]

    # Read numbers from the file
    numbers = read_file(file_name)

    if not numbers:
        print("No valid numbers found in the file. Exiting.")
        sys.exit(1)

    # Start Calculation Time
    calculation_start_time = time.time()

    # Compute Statistics
    count_output = len(numbers)
    mean_output = calculate_mean(numbers)
    median_output = calculate_median(numbers)
    mode_output = calculate_mode(numbers)
    variance_output = calculate_variance(numbers, mean_output)
    std_output = calculate_standard_deviation(variance_output)

    results = (count_output,mean_output, median_output, mode_output, variance_output, std_output)

    # Determine Calculation Time
    calculation_end_time = time.time()
    calculation_time = calculation_end_time - calculation_start_time

    # Calculate Elapsed Time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print and save results
    print_results(results,elapsed_time,calculation_time,file_name)

if __name__ == "__main__":
    main()
