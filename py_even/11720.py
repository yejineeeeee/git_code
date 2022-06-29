n = input()
nums = input()
tot = 0
for i in nums:
    tot += int(i)
print(tot)

#
for i in range(n):
    tot += int(nums[i])
print(tot)