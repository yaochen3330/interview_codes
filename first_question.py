from collections import defaultdict
import bisect

def min_subsequences(source: str, target: str) -> int:
    # map source character position
    char_positions = defaultdict(list)
    for index, char in enumerate(source):
        char_positions[char].append(index)

    # Ensure character exist
    if any(char not in char_positions for char in target):
        return -1

    subseq_count = 0
    target_index = 0
    target_length = len(target)
    
    while target_index < target_length:
        subseq_count += 1
        current_pos = -1

        while target_index < target_length:
            char = target[target_index]
            positions = char_positions[char]
            pos = bisect.bisect_right(positions, current_pos)
            
            if pos == len(positions):
                break
            
            current_pos = positions[pos]
            target_index += 1
        
    return subseq_count
