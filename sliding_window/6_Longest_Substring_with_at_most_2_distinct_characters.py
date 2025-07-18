
# Longest Substring with at most 2 distinct characters

# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

def longest_substrig_with_2_distinct_chars(string):

    frequency = {}

    max_length = 0

    window_start = 0

    for window_end in range(len(string)):

        current = string[window_end]

        frequency[current] = frequency.get(current, 0)+1

        while len(frequency.keys()) > 2:

            frequency[string[window_start]]-=1

            if frequency[string[window_start]] == 0:
                del frequency[string[window_start]]

            window_start+=1
        
        max_length = max(max_length, window_end-window_start+1)
    
    return max_length


# Example usage:
string ="ararrccaraccc"
result = longest_substrig_with_2_distinct_chars(string)
print("Longest substring with at most {} ".format(result))
# Output: Longest substring with at most 2 distinct characters: 5
        