'''
This script is used to provide a word count for different text files
1. Reads the file (ex: TC1.txt, TC2.txt, etc..)
2. Calculates frequency for each word
3. Performs time elasped and time calculation 
4. Prints outputs to WordCountResults.txt amd console
'''
import sys
import time

# Read File
def read_file(file_name):
    """
    Reads a file that contains a list of words.
    If the file contains any invalid values, it will print out an warning. 
    """
    words = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            # Generate warning for numeric values
            try:
                number = float(line)  # If conversion succeeds, it's a number
                print(f"Warning: Found a number: '{number}'. Ignored.")

            except ValueError:
                # If conversion fails, treat it as text (words)
                words.extend(line.split())  # Split the line into words and add to words list
    return words

# Identify distinct words and their frequency
def find_frequency_distinct_words(words):
    '''
    This function is used to identify distinct words and
    determine the frequency of each word.
    '''
    word_frequency = []

    for word in words:
        # Check if the word already exists
        found = False
        for i, word in enumerate(word_frequency):
            if word_frequency[i][0] == word:
                # Word found, increment its frequency
                word_frequency[i] = (word, word_frequency[i][1] + 1)
                found = True
                break

        # If the word wasn't found, add it to the list with a count of 1
        if not found:
            word_frequency.append((word, 1))

    return word_frequency


# Printing Results
def print_results(results,elapsed_time,calculation_time,file_name):
    '''
    Print results in console and output file WordCountResults.txt.
    '''
    # Create the header for the results
    result_output = f"{'Row Labels':<30}{f'Count of {file_name}':<15}\n"

    # Initialize the total frequency
    total_frequency = 0


    # Add the results for each word
    for word, word_frequency in results:
        result_output += f"{word:<30}{word_frequency:<10}\n"
        total_frequency += word_frequency # Calculate the total frequency

    # Print Grand Total (Total Frequency)
    result_output += f"{'Grand Total: ':<1}{total_frequency:<15}\n"

    result_output += f"\nTIME ELAPSED FOR EXECUTION: {elapsed_time:.6f} seconds\n"
    result_output += f"TIME FOR DATA CALCULATION: {calculation_time:.6f} seconds\n"

    print(result_output) # Print to console

    # Write to file
    with open("WordCountResults.txt", 'w', encoding='utf-8') as file:
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
        print("Usage: python word_count.py <fileWithData.txt>")
        sys.exit(1)

    file_name = sys.argv[1]

    # Read words from the file
    words = read_file(file_name)

    if not words:
        print("No valid words found in the file. Exiting.")
        sys.exit(1)

    # Start Calculation Time
    calculation_start_time = time.time()

    # Comput frequency for distinctive words
    word_frequency = find_frequency_distinct_words(words)

    results = word_frequency

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
