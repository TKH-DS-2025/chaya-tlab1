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
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    file.close()
    
   # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    new_data = filter_nondigits(data)
    print (new_data)
    # Use the `new_data` variable to plot the data using matplotlib
    # and save the plot to the "images" folder as "phase0.png"
       

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    plt.plot(new_data)
    plt.xlabel('Time')
    plt.ylabel('Heart Rate')
    plt.title('Heart Rate Over Time')
    plt.grid(True)
    # Ensure the images directory exists before saving
    plt.savefig('images/phase0.png')

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = (average(new_data))
    # convert the max and std_dev to float as well
    # to match the return type
    # this will allow you to return all 3 values as floats
    # and not integers
    max_hr = (max(new_data))
    # calculate the standard deviation of the heart rate data
    # using the standard_deviation function you've written
    std_dev_hr = (round(standard_deviation(new_data)))
    # print the values to the console
    
    
   

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print(run("data/phase0.txt"))


