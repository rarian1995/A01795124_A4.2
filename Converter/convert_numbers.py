'''
This script is used to convert decimal numbers into binary or hexadecimal values
1. Reads the file (ex: TC1.txt, TC2.txt, etc..)
2. Converts decimal numbers into binary or hexadecimal values
3. Performs time elasped and time calculation 
4. Prints outputs to ConvertionResults.txt amd console
'''
import sys
import time

# Read File
def read_file(file_name):
    """
    Reads a file that contains a list of items.
    If the file contains any invalid values, it will print out a warning. 
    It will also process negative numbers and try to convert them to binary and hexadecimal.
    """
    numbers = []

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            # Check for invalid character input
            try:
                number = int(line)
                # Appends the valid numbers to the list
                numbers.append(number)

            except ValueError:
                # Handle non-numeric input
                print(f"Warning: Invalid Item Found in the File: {line}")
    return numbers


# Perform Conversions
def convert_binary(number):
    '''
    This function performs the conversion from decimal to binary.
    '''
    # Initiate strings
    binary_output = ""

    # Test to see if number is 0
    if number == 0:
        return "0"

    # Handle negative numbers
    sign = "-" if number < 0 else ""
    number = abs(number)

    # Calculate binary values
    while number > 0:
        remainder = number % 2
        binary_output = str(remainder) + binary_output
        number = number // 2

    return sign + binary_output

def convert_hexadecimal(number):
    '''
    This function performs the conversion from decimal to hexadecimal.
    '''
    # Initiate strings
    hex_digits = "0123456789ABCDEF"
    hexadecimal_output = ""

    #Test to see if number is 0
    if number == 0:
        return "0"

    # Handle Negative Values
    sign = "-" if number < 0 else ""
    number = abs(number)

    # Calculate hexadecimal value
    while number > 0:
        remainder = number % 16
        hexadecimal_output = hex_digits[remainder] + hexadecimal_output
        number = number // 16

    return sign + hexadecimal_output

# Printing Results
def print_results(results,elapsed_time,calculation_time):
    '''
    Print results in console and output file ConvertionResults.txt.
    '''
    # Create the header for the results
    result_output = f"{'':<10}{'ITEM':<15}{'BINARY':<30}{'HEXADECIMAL':<15}\n"

    # Add the results for each item in the list `results`
    for idx, (item_value, binary_value, hex_value) in enumerate(results, 1):
        result_output += f"{idx:<10}{int(item_value):<15}{binary_value:<30}{hex_value:<15}\n"
    result_output += f"\nTIME ELAPSED FOR EXECUTION: {elapsed_time:.6f} seconds\n"
    result_output += f"TIME FOR DATA CALCULATION: {calculation_time:.6f} seconds\n"
    print(result_output) # Print to console

    # Write to file
    with open("ConvertionResults.txt", 'w', encoding='utf-8') as file:
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
        print("Usage: python convert_numbers.py <fileWithData.txt>")
        sys.exit(1)

    file_name = sys.argv[1]

    # Read numbers from the file
    numbers = read_file(file_name)

    if not numbers:
        print("No valid numbers found in the file. Exiting.")
        sys.exit(1)

    # Start Calculation Time
    calculation_start_time = time.time()

    # Apply Conversions
    results = []

    for number in numbers:
        binary_output = convert_binary(number)
        hexadecimal_output = convert_hexadecimal(number)
        results.append((number, binary_output, hexadecimal_output))

    # Determine Calculation Time
    calculation_end_time = time.time()
    calculation_time = calculation_end_time - calculation_start_time

    # Calculate Elapsed Time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print and save results
    print_results(results,elapsed_time,calculation_time)

if __name__ == "__main__":
    main()
