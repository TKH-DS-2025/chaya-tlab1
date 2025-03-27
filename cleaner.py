def filter_nondigits(data: list) -> list:
    """
    INSERT DOCSTRING HERE
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






 



