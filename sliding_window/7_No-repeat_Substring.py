# No-repeat Substring

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def no_repeating_chars_substring(string):

    frequency = {}

    max_length = 0
    window_start = 0

    for window_end in range(len(string)):
        print(frequency)

        current = string[window_end]

        frequency[current] = frequency.get(current, 0)+1

        if frequency[current]> 1:
            frequency[current]-=1
            window_start+=1

            max_length = max(max_length, window_end-window_start+1)


            frequency = {}
            
        
        
    return max_length


# Example usage:
string ="aabccbb"
result = no_repeating_chars_substring(string)
print("Longest substring with at most {} ".format(result))
# Output: Longest substring with at most 2 distinct characters: 5
        
