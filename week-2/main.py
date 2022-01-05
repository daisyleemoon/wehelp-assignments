# 要求一：函式與流程控制

# def calculate(min, max):
#     print((max + min) * (max - min + 1)/2)
# # 請用你的程式補完這個函式的區塊
# calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
# calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

# 要求二：Python 字典與列表、JavaScript 物件與陣列

def avg(data):

	# apple = count_info["employees"][0]["salary"]
	# print(f"{apple}")
	# for employee in data["employees"]:
	# 	print(employee["salary"])
	# 	print(employee)
	for i in range(data["count"]):
		print(data["employees"][i]["salary"])

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
