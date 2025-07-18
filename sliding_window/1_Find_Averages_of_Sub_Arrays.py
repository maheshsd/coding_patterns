#Find Averages of Sub Arrays
#https://leetcode.com/problems/maximum-average-subarray-i/

def find_averages_of_sub_arrays(k, arr):
    window_sum = 0
    window_start = 0
    result = []

    for window_end in range(len(arr)):
        window_sum+= arr[window_end]

        if window_end >= k-1:
            result.append(window_sum/k)
        
        window_sum-= arr[window_start]
        window_start+=1
    
    return result


# Example usage:
array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
averages = find_averages_of_sub_arrays(k, array)
print("Averages of sub-arrays of size K: ", averages)