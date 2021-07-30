# -*- coding: utf-8 -*-

#做些简单的，不论出处的小题目


# 1、题目描述：
# 手机的九宫格输入法中，输入数字的键位是可以和字母键位对应的。如“2”对应“ABC”，“9”对应“WXYZ”，现假设“1”和“0”为空字符，以此规则试设计一个程序，将单词用一串数字来进行表示。
# 举例
# 输入：cat（不区分大小写）
# 输出：228
def word2num(word):
	dic = {'ABCabc':'2', 
	'DEFdef':'3', 
	'GHIghi':'4', 
	'JKLjkl':'5', 
	'MNOmno':'6', 
	'PQRpqr':'7', 
	'STUVstuv':'8', 
	'WXYZwxyz':'9'}
	num = ''
	for letter in word:
		for key, value in dic.items():
			if letter in key:
				num = num + value
	num = int(num)
	return num
if __name__ == '__main__':
	word = input('please input a word:')
	result = word2num(word)	
	print(result)