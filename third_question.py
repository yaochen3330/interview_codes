from itertools import combinations

def calculate_max_weight(n, a):
    def mean(subarray):
        total = sum(subarray)
        return total / len(subarray)
    
    def median(subarray):
        subarray.sort()
        length = len(subarray)
        mid = length // 2
        if length % 2 == 1:
            return subarray[mid]
        else:
            return (subarray[mid - 1] + subarray[mid]) / 2
    
    max_weight = float('-inf')
    
    # 生成所有非空子序列
    for size in range(1, n + 1):
        for indices in combinations(range(n), size):
            subarray = [a[i] for i in indices]
            m = mean(subarray)
            med = median(subarray)
            weight = m - med
            
            # 打印中位数、均值、权值及子序列
            print(f"Subarray: {subarray}")
            print(f"Mean: {m:.4f}")
            print(f"Median: {med:.4f}")
            print(f"Weight: {weight:.4f}\n")
            
            if weight > max_weight:
                max_weight = weight
    
    return max_weight

# 示例输入
n = 4
a = [1, 3, 5, 9]
print(f"Max Weight: {calculate_max_weight(n, a):.4f}")
