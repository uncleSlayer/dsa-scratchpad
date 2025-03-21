
nums = [1, 1, 2, 3, 3, 3]

k = 2

count = {}

for number in nums:

    count[number] = count.get(number, 0) + 1


answer = sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]
print([x[0] for x in answer])