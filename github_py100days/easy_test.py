# -*- coding:UTF-8 -*-
#from: https://github.com/jackfrued/Python-100-Days/blob/master/%E5%85%AC%E5%BC%80%E8%AF%BE/%E6%96%87%E6%A1%A3/%E5%B9%B4%E8%96%AA50W%2B%E7%9A%84Python%E7%A8%8B%E5%BA%8F%E5%91%98%E5%A6%82%E4%BD%95%E5%86%99%E4%BB%A3%E7%A0%81/%E5%B9%B4%E8%96%AA50W%2B%E7%9A%84Python%E7%A8%8B%E5%BA%8F%E5%91%98%E5%A6%82%E4%BD%95%E5%86%99%E4%BB%A3%E7%A0%81.md

'''
#列表
numbers = [x for x in range(1, 11)]
print(numbers)
print("\n\n")


#双色球随机选号
from random import randint, sample

def generate():
    """生成一组随机号码"""
    red_balls = [x for x in range(1, 34)]
    selected_balls = sample(red_balls, 6)   #sample(list, k)返回一个长度为k新列表，新列表存放list所产生k个随机唯一的元素
    # print(selected_balls)
    selected_balls.sort()   #从小到大排列
    # print(selected_balls)
    selected_balls.append(randint(1, 16))   #append() 方法用于在列表末尾添加新的对象       randint()可以生成1个随机数
    # print(selected_balls)
    return selected_balls

def display(balls):
    """输出一组双色球号码"""
    # print(list(enumerate(balls)))   #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
    for index, ball in enumerate(balls):   
        print(f'{ball:0>2d}', end=' ')  #2d表示使用填充（默认为空白）将格式设置为2个字符   0>表示使用0作为填充，并右调整结果
        if index == len(balls) - 2:
            # print(len(balls)-2)
            print('|', end=' ')
    # print()

num = int(input('随机选几注: '))
for _ in range(num):    #’_’ 是一个循环标志，也可以用i，j 等其他字母代替，下面的循环中不会用到，起到的是循环此数的作用
    display(generate())


#给定一个数组s1，输入一组数s2，求s2中s1的个数
s1=[1,9,18,33]
s2=input("请输入一组数：")  #输入内容以空格隔开
s2=[int(v) for v in s2.split(" ")]  #去掉空格项，组成数组
print(s1)
print(s2)
count=0
for i in s1:
    for j in s2:
        if i==j:
            count+=1
print("s2中有s1的数：{}".format(count))



#找出数组中超过数组长度一半的数字
s=[1,9,18,2,6,33,0,44]
a=[]
for i in s:
    if i >len(s)/2:
        a.append(i)
print(a)

'''





