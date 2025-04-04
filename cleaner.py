def filter_nondigits(data: list) -> list:
  
    """
    Filter out non-digit characters from the list of strings.

    Args:
        data (list[str]): list of strings to be filtered
    Returns:
        list[int]: a list of integers containing only the digit characters from the input list
    """
    new_data = []
    for x in data:
       print("orginial line, x: ", x)
       x = x.strip()
       print("stripped line, x: ", x) 
       if x.isdigit():
           new_data.append(int(x))

    return new_data


print(filter_nondigits(["1", "2", "3", "4", "5", "6", "7",])) 






 



