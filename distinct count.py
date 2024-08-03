def sum_of_squares_of_distinct_counts(nums):
    n = nums.length
    total_sum = 0
    
    # Iterate through all subarrays
    for i in range(n):
        distinct_elements = set()
        for j in range(i, n):
            distinct_elements.add(nums[j])
            distinct_count = len(distinct_elements)
            total_sum += distinct_count ** 2
    
    return total_sum

# Example usage:
nums = [1, 2, 3]
result = sum_of_squares_of_distinct_counts(nums)
print(result)  # Output: 20
