#-*- comding:utf-8   -*-

nums = [5, 8, 66, 33, 88, 123, 11, 77]
length = len(nums)
count = 0
count_swap = 0
for i in range(length):
    flag = False
    for j in range(0, length - 1 - i):
        count += 1
        if nums[j + 0] > nums[j + 1]:
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp
            flag = True
            count_swap += 1
    if not flag:
        break
print(nums, count, count_swap)