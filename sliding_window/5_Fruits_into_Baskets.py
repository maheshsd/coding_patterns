# Fruits into Baskets
# https://leetcode.com/problems/fruit-into-baskets/

def max_fruits_in_2_basket(fruits):
    fruits_frequency = {}

    window_start = 0
    
    max_length = 0

    for window_end in range(len(fruits)):
        fruits_frequency[fruits[window_end]] = fruits_frequency.get(fruits[window_end], 0)+1

        while len(fruits_frequency.keys()) > 2:

            fruits_frequency[fruits[window_start]]-=1

            if fruits_frequency[fruits[window_start]] == 0:
                del fruits_frequency[fruits[window_start]]

            window_start+=1
        
        max_length = max(max_length, window_end-window_start+1)
    return max_length



# Example usage:
string ="araccaraccc"
result = max_fruits_in_2_basket(string)
print("Longest substring with at most {} ".format(result))
# Output: Longest substring with at most 2 distinct characters: 4
        