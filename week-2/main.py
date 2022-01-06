# 要求一：函式與流程控制

def calculate(min, max):
    print((max + min) * (max - min + 1)/2)
# 請用你的程式補完這個函式的區塊
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

# 要求二：Python 字典與列表、JavaScript 物件與陣列

def avg(data):
	if data["count"] != len(data["employees"]):
		print("account information invalid")
	else:
		total_salary = 0
		for i in range(data["count"]):
			total_salary += data["employees"][i]["salary"]
	print(total_salary / len(data["employees"]))

avg({
	"count": 3,
	"employees": [
		{
			"name": "John",
			"salary": 30000
		},
		{
			"name": "Bob",
			"salary": 60000
		},
		{
			"name": "Jenny",
			"salary": 50000
		}
	]
})  # 呼叫 avg 函式

# 要求三：演算法
def maxProduct(nums):
	if len(nums) < 2:
		print(f"invalid input")
	max1 = nums[0]
	max2 = nums[1]
	min1 = nums[0]
	min2 = nums[1]
	if nums[1] > nums[0]:
		max1, max2 = nums[1], nums[0]
	if nums[1] < nums[0]:
		min1, min2 = nums[1], nums[0]
		for i in range(2, len(nums)):
			if nums[i] > max2:
				if nums[i] > max1:
					max1, max2 = nums[i], max1
				else:
					max2 = nums[i]
			if nums[i] < min2:
				if nums[i] < min1:
					min1, min2 = nums[i], min1
				else:
					min2 = nums[i]

	product1 = max1 * max2
	product2 = min1 * min2
	result = product1 if product1 > product2 else product2
	print(result)


maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([-1, -2, 0])  # 得到 2


# 要求四 ( 請閱讀英文 )：演算法

def twoSum(nums, target):
	copy_nums = sorted(nums)
	head = copy_nums[0]
	tail = copy_nums[len(copy_nums) - 1]
	while copy_nums.index(tail) - copy_nums.index(head) > 1:
		if head + tail > target:
			tail = copy_nums[copy_nums.index(tail)-1]
		if head + tail < target:
			head = copy_nums[copy_nums.index(head)+1]
		if head + tail == target:
			head, tail = head, tail
	if head + tail == target:
		return [nums.index(head), nums.index(tail)]
	else:
		return "not found"

result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9

# 要求五 ( Optional )：演算法

def maxZeros(nums):
	counter = 0
	max_len = 0
	for num in nums:
		if num == 0:
			counter += 1
			if counter > max_len:
				max_len = counter
		if num == 1:
			counter = 0
	print(max_len)

maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
maxZeros([0, 0, 0, 1, 1])  # 得到 3
