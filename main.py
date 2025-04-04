"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').
    
    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """
    data = []

    # open file using file I/O and read it into the `data` list
    file = open(filename)
    for line in file:
        data.append(line.strip())
    
    
   # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    new_data = filter_nondigits(data)

    # Use the `new_data` variable to plot the data using matplotlib
    # and save the plot to the "images" folder as "phase0.png"
       

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    plt.plot(new_data)
    plt.xlabel('Time')
    plt.ylabel('Heart Rate')
    plt.title('Heart Rate Over Time')
    plt.grid(True)
    plt.xlim(0, len(new_data) - 1)  # Set x-axis limits to match the data length
    plt.ylim(min(new_data) - 5, max(new_data) + 5)  # Add some padding to y-axis limits
    # Ensure the images directory exists before saving
    plt.savefig('images/phase0.png')
    plt.clf()  # Clear the current figure to avoid overlapping plots
    plt.close()  # Close the current figure to free up memory
   


    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = (average(new_data))
    # convert the max and std_dev to float as well
    # to match the return type
    # this will allow you to return all 3 values as floats
    # and not integers
    max_hr = (max(new_data))
    # calculate the standard deviation of the heart rate data
    # using the standard_deviation function you've written
    std_dev_hr = (standard_deviation(new_data))
    # print the values to the console
    print(f"Average Heart Rate: {avg_hr:.2f}")
    print(f"Maximum Heart Rate: {max_hr:.2f}")
    print(f"Standard Deviation of Heart Rate: {std_dev_hr:.2f}")    
    
   

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print(run("data/phase0.txt"))
    print(run("data/phase1.txt"))
    print(run("data/phase2.txt"))
    print(run("data/phase3.txt"))




