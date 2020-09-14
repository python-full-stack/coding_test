## 준영
def twoSum(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in num[i + 1:]:
            return nums.index(n), nums[i+1:].index(complement) + (i +1)

num = [2,7,11,15]
target = 18

result = twoSum(num, target)
print(result)

## 영보

## 승범