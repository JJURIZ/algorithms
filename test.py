# First function - Finds the middle of the array.
# Using the midpoint recursively calls the function to continue splitting the array. 
# When the array length is 1 the recusrive loop breaks and returns the array.

def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = int(len(array) // 2)

    left, right = merge_sort(array[:middle]), merge_sort(array[middle:])
    print(f"printing left = {left}, printing right = {right}, printing middle = {middle}", )
    return merge(left, right)
    
def merge(left, right):
    result = [] # Stores the final sorted result
    left_idx = right_idx = 0 # Counters

    while left_idx < len(left) and right_idx < len(right):
        # print(f"this is left index = {left_idx} and this is right index = {right_idx}")

        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
            # print(f"This is printing the result inside left_idx: {result}")
        else:
            result.append(right[right_idx])
            right_idx += 1
            # print(f"This is printing the result right_idx: {result}")
            
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

print(merge_sort([5,2,1,89,4,76,3,22,43]))