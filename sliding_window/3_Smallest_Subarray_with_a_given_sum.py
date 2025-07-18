# Smallest Subarray with a given sum

# https://leetcode.com/problems/minimum-size-subarray-sum/

def smallest_subarray_with_given_sum(arr, target_sum):
    min_length = float('inf')
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= target_sum:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    return min_length if min_length != float('inf') else 0

# Example usage:
arr = [2, 1, 5, 2, 3, 2]
target_sum = 7
result = smallest_subarray_with_given_sum(arr, target_sum)
print("Smallest subarray length with sum at least {}: {}".format(target_sum, result))
# Output: Smallest subarray length with sum at least 7: 2