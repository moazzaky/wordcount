text_list = ['sad', 'man', 'sad', 'man']

nums = {}

for word in text_list:
    if word in nums.keys():
        num = nums.get(word)
        num +=1
        nums[word] = num
    else:
        nums[word] = 1

print(nums)
