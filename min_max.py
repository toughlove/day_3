def find_max_min(Arr):
    max_min = []
    minimum = maximum = Arr[0]
    for item in Arr[1:]:
        if item < minimum: 
            minimum = item
        else: 
            if item > maximum:
              maximum = item
    max_min.append(minimum)
    max_min.append(maximum)
    return (max_min)
  
  