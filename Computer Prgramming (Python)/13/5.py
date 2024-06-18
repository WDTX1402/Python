def is_subset_sum(arr, n, subset, v):
    """
    Recursive function to solve subset sum problem.
    :param arr: List of integers.
    :param n: Length of the list.
    :param subset: Current subset being considered.
    :param v: A list that stores the valid subsets.
    :return: Boolean indicating if a subset with sum 0 exists.
    """
    # Base case: if no remaining elements
    if n == 0:
        if sum(subset) == 0 and len(subset) > 0:
            v.append(subset.copy())
            return True
        return False

    # Choice 1: Exclude current element
    exclude = is_subset_sum(arr, n-1, subset, v)
    
    # Choice 2: Include current element
    subset.append(arr[n-1])
    include = is_subset_sum(arr, n-1, subset, v)
    subset.pop()  # Revert the change

    return exclude or include

def find_zero_sum_subsets(arr):
    valid_subsets = []
    is_subset_sum(arr, len(arr), [], valid_subsets)
    if valid_subsets != []:
        return f"Yes, {valid_subsets}"
    else:
        return f"No"

# Test
arr1 = [-7, -3, -2, 5, 7]
arr2 = [2.-3,5,8,11,23,-1]
result = find_zero_sum_subsets(arr1)
print(result)
