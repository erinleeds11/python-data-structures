def bisection_search_iterative(arr, target):
    start_idx = 0
    stop_idx = len(arr)-1
    while start_idx < stop_idx:
        middle_idx = (stop_idx + start_idx) //2
        if target == arr[middle_idx]:
            return middle_idx
        elif target < arr[middle_idx]:
            stop = middle_idx - 1
        elif target > arr[middle_idx]:
            start = middle_idx + 1 
    return "Not found"
        
def bisection_search_recursive(arr, target, start, stop):
    if start > stop:
        return "Not found"
    else:
        if target == arr[middle_idx]:
                return middle_idx
        elif target < arr[middle_idx]:
                return bisection_search_recursive(arr, target, start, middle_idx -1)
        else target > arr[middle_idx]:
                return bisection_search_recursive(arr, target, middle_idx+1, stop)
    
        

