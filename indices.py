def calculate_indices(num, nums):
    set_nums = set(nums)
    set_num = set(num)
    
    answer1 = sum(1 for n in num if n in set_nums)
    answer2 = sum(1 for n in nums if n in set_num)
    
    return [answer1, answer2]

num_1 = [2, 3, 2]
nums_1 = [1, 2]
print(calculate_indices(num_1, nums_1))

num_2 = [4, 3, 2, 3, 1]
nums_2 = [2, 2, 5, 2, 3, 6]
print(calculate_indices(num_2, nums_2))
