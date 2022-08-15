nums = [10, 20, 30, 40]


def sum(nums):
    summa = 0
    for i in nums:
        summa += i
    return summa


def avg(nums):
    summa = 0
    for i in nums:
        summa += i
    return summa / len(nums)


def maximum(nums):
    maxx = nums[0]
    for i in nums:
        if i > maxx:
            maxx = i
    return maxx


def minimum(nums):
    minn = nums[0]
    for i in nums:
        if i < minn:
            minn = i
    return minn


def difference(nums):
    minn = nums[0]
    maxx = nums[0]
    for i in nums:
        if i > maxx:
            maxx = i
    for i in nums:
        if i < minn:
            minn = i
    return maxx - minn


def more_than_x(nums, x):
    for i in nums:
        if i > x:
            print(i)
    return


def first_more_than_x(nums, x):
    for i in nums:
        if i > x:
            print(i)
            break
    return


def sum_more_than_x(nums, x):
    suma = 0
    for i in nums:
        if i > x:
            suma += i
    return suma


def count_more_than_x(nums, x):
    count = 0
    for i in nums:
        if i > x:
            count += 1
    return count


def print_divisible(nums, x):
    for i in nums:
        if i % x == 0:
            print(i)
    return


def fisrt_divisible(nums, x):
    for i in nums:
        if i % x == 0:
            print(i)
            break
        else:
            return None



def common(numbers1, numbers2):

    for i in numbers1:
        for x in numbers2:
            if i == x:
                print(i)
    return
numbers1 = [1, 2, 3, 4, 6, 8]
numbers2 = [3, 6, 7, 34, 4, 1]
common(numbers1, numbers2)
