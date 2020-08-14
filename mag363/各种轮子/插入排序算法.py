#-*- comding:utf-8   -*-

def interposition():
    origin = [1,9,8,5,6]
    nums = [0] + origin
    length =len(nums)
    for i in range(2, length):
        nums[0] = nums[i] #哨兵
        j = i -1
        if nums[j] > nums[0]:
            print(i,j,nums[j],nums[0],'看看',nums)
            while nums[j] > nums[0]:
                nums[j+1] = nums[j]
                print('开始',nums)
                j -= 1
            nums[j+1] = nums[0]

    print(nums)