from itertools import combinations

def two_characters(s):
    max_length = 0
    unique_chars = list(set(s))
    
    if len(unique_chars) < 2:
        return 0
        
    for char1, char2 in combinations(unique_chars, 2):
        filtered = [c for c in s if c == char1 or c == char2]
        
        is_valid = True
        for i in range(len(filtered) - 1):
            if filtered[i] == filtered[i+1]:
                is_valid = False
                break
        
        if is_valid:
            max_length = max(max_length, len(filtered))
            
    return max_length