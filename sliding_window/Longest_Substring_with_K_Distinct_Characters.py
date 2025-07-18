
# Longest Substring with K Distinct Characters (medium)

# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

def Longest_substring_with_k_distinct(string, k):
    longest = 0
    frequency = {}

    window_start = 0

    for window_end in range(len(string)):
        frequency[string[window_end]] = frequency.get(string[window_end], 0)+1

        while len(frequency.keys()) > k:
            frequency[string[window_start]] = frequency.get(string[window_start])-1
            if frequency[string[window_start]] == 0:
                del frequency[string[window_start]] 
            window_start += 1
        
        longest = max(longest, window_end-window_start+1)
    
    return longest


# Example usage:
string ="araccaraccc"
k = 1
result = Longest_substring_with_k_distinct(string, k)
print("Longest substring with at most {} distinct characters: {}".format(k, result))
# Output: Longest substring with at most 2 distinct characters: 4
        
