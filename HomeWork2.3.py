nums = list()
count = int(input())
i = 0

while i < count:
    a = int(input())
    nums.append(a)
    i += 1

total_sum = 0

for i in nums:
    total_sum += i
print(f"Total sum is: {total_sum}")

AVG = total_sum / len(nums)

print(f"AVG is: {round(AVG, 2)}")

maximum = nums[0]

for i in nums:
    if i > maximum:
        maximum = i
print(f"Maximum is: {maximum}")

minimum = nums[0]

for i in nums:
    if i < minimum:
        minimum = i
print(f"Minimum is: {minimum}")
