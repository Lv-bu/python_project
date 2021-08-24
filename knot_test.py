# -*- coding: utf-8 -*-

# Given an integer list containing digits from [0, 9], the task is to print all possible letter combinations that the numbers could represent. 
# A mapping of digit to letters (just like on the telephone buttons) is being followed. Note that 0 and 1 do not map to any letters. 
# Example ：
# Input: [2,3] Output: ad ae af bd be bf cd ce cf                Input [9] Output: w x y z



def letter_Combinations(num):

	# 数字对应的字符列表
	dic = {2: ['a', 'b', 'c'],
		3: ['d', 'e', 'f'],
		4: ['g', 'h', 'i'],
		5: ['j', 'k', 'l'],
		6: ['m', 'n', 'o'],
		7: ['p', 'q', 'r', 's'],
		8: ['t', 'u', 'v'],
		9: ['w', 'x', 'y', 'z'],
		}
	
	result_list = []

	if len(num) == 0: 
		return []

	if len(num) == 1:
		return dic[int(num[0])]
	
	
	# print(num[1:])
	# print(num[0])
	letter_result = letter_Combinations(num[1:])
	# print(letter_result)
	# result是一个数组列表，遍历后字符串操作，加入列表
	for r in letter_result:
		for j in dic[int(num[0])]:
			result_list.append(j + r)


	# print(result_list)
	return result_list


if __name__ == '__main__':
    print(letter_Combinations(input("请输入2-9的数字：")))