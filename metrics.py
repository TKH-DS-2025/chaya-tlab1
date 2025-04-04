def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    #average = 0
    #if data == []:
        #return []
    #for i in data:
        #average += i
    #return average / len

    if not data:
        return []
    return round(sum(data) / len(data), 2)
   
   
   
   
result = [1, 2, 3, 4, 5, 6, 7]
print(average(result))





def maximum(data: list) -> float:
    """
    Calculate maximum value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the maximum of this list
    """
    if data == []:
        return []
    maximum_v = 0 
    for i in data:
        if i > maximum_v:
            maximum_v = i
    return maximum_v 
    
result = [1, 2, 3, 4, 5, 6, 7]
print(maximum(result))

def variance(data: list) -> float:
    """
    Calculate variance value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the variance of this list
    """
 
    #if data == []:
        #return []
    #variance = 0
    #for i in data:
        #variance += (i - average(data)) ** 2
    #return variance / len(data)

    if not data:
        return []
    mean = average(data)
    return round(sum((x - mean) ** 2 for x in data) / len(data), 2)

result = [1, 2, 3, 4, 5, 6, 7]
print(variance(result))    

def standard_deviation(data: list) -> float:
    """
    Calculate standard deviation of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the standard deviation of this list
    """

    if data == []:
        return []
    standard_deviation = 0
    for i in data:
        standard_deviation += (i - average(data)) ** 2
    return round(((standard_deviation / len(data))) ** 0.5,2)
    
result = [1, 2, 3, 4, 5, 6, 7]
print(standard_deviation(result))