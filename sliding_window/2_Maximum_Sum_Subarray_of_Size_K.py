# Maximum Sum Subarray of Size K

# https://leetcode.com/problems/largest-subarray-length-k/

def max_sum_subarray_of_size_k(arr, k):
    max_sum = float('-inf')
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum

# Example usage:
arr = [2, 1, 5, 1, 3, 2]
k = 3
result = max_sum_subarray_of_size_k(arr, k)
print("Maximum sum of subarray of size {}: {}".format(k, result))
# Output: Maximum sum of subarray of size 3: 9