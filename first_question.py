def min_subsequences(source: str, target: str) -> int:
    from collections import defaultdict
    import bisect

    # Map characters in source to their positions
    char_positions = defaultdict(list)
    for index, char in enumerate(source):
        char_positions[char].append(index)

    # Check if all characters in target are in source
    for char in target:
        if char not in char_positions:
            return -1

    subseq_count = 0
    target_index = 0
    n = len(target)
    
    while target_index < n:
        subseq_count += 1
        current_position = -1
        
        while target_index < n:
            char = target[target_index]
            positions = char_positions[char]
            pos = bisect.bisect_right(positions, current_position)
            
            if pos == len(positions):
                break  # Need a new subsequence
            
            current_position = positions[pos]
            target_index += 1
        
    return subseq_count

# Example usage
if __name__ == "__main__":
    source = "abc"
    target = "abcbc"
    print(min_subsequences(source, target))  # Output: 2

    source = "abc"
    target = "acdbc"
    print(min_subsequences(source, target))  # Output: -1

    source = "xyz"
    target = "xzyxz"
    print(min_subsequences(source, target))  # Output: 3
