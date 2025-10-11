# Erya Anom
# Statistics Exercise

import statistics

def read_data(filename):
    """
    Reads a set of numbers from a specified file and returns them as a list.

    :param filename: str - name of the file to read the data from
    :return: list - list of numbers read from the file
    """
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                numbers.append(float(line.strip()))
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    
    return numbers

def display_statistics(number_list):
    """
    Displays basic statistics of a list of numbers.
    """
    if not number_list:
        print("The list of numbers is empty.")
        return

    mean = statistics.mean(number_list)
    median = statistics.median(number_list)
    try:
        mode = statistics.mode(number_list)
    except statistics.StatisticsError:
        mode = "No unique mode"
    
    variance = statistics.pvariance(number_list)  # Population Variance
    std_dev = statistics.pstdev(number_list)      # Population Standard Deviation

    # Display the statistics
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")

def main():
    """
    Main function to execute the program.
    It will prompt for the filename, read data, and display statistics.
    """
    filename = input("Enter the filename containing the numbers: ")
    number_list = read_data(filename)
    display_statistics(number_list)

if __name__ == "__main__":
    main()
