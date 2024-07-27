from itertools import combinations
import statistics

def calculate_max_weight(n, a):
    def mean(subarray):
        return sum(subarray) / len(subarray)
        
    def median(subarray):
        return statistics.median(subarray)
    
    max_weight = float('-inf')
    
    for size in range(1, n + 1):
        for indices in combinations(range(n), size):
            subarray = [a[i] for i in indices]
            m = mean(subarray)
            med = median(subarray)
            weight = m - med
            
            # Print subarray details
            print(f"Subarray: {subarray}")
            print(f"Mean: {m:.4f}")
            print(f"Median: {med:.4f}")
            print(f"Weight: {weight:.4f}\n")
            
            # Update max_weight 
            if weight > max_weight:
                max_weight = weight
    
    return max_weight
