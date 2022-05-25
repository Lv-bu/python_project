# -*- coding:utf-8 -*-

'''
# super() 函数是用于调用父类(超类)的一个方法
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')
    
    def bar(self,message):
        print ("%s from Parent" % message)
class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild,self).__init__()    
        print ('Child')
        
    def bar(self,message):
        super(FooChild, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)
 
if __name__ == '__main__':
    fooChild = FooChild()
'''
# 函数式编程：https://docs.python.org/zh-cn/3.7/howto/functional.html
# https://www.cnblogs.com/bfcs/p/10740292.html
# 1、FizzBuzz问题：打印数字1到100, 3的倍数打印“Fizz”, 5的倍数打印“Buzz”, 既是3又是5的倍数的打印“FizzBuzz”
#"fizz"[ x % 3 * 4:]的意思为，如果冒号左边的答案大于等于字符长度（“fizz”“buzz”长度为4）则不输出
# print(' '.join(["fizz"[x % 3 * 4:]+"buzz"[x % 5 * 4:] or str(x) for x in range(1, 101)]))
# 2、一行代码输出特定字符"Love"拼成的心形
# print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
#3、一行代码打印九九乘法表
# print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))
# #4、一行代码计算出1-100之间的素数(两个版本)
# print(' '.join([str(item) for item in filter(lambda x: not [x % i for i in range(2, x) if x % i == 0], range(2, 101))]))
# print(' '.join([str(item) for item in filter(lambda x: all(map(lambda p: x % p != 0, range(2, x))), range(2, 101))]))
# #5、一行代码输出斐波那契数列
# print([x[0] for x in [(a[i][0], a.append([a[i][1], a[i][0]+a[i][1]])) for a in ([[1, 1]], ) for i in range(30)]])
# #6、一行代码实现快排算法
# qsort = lambda arr: len(arr) > 1 and qsort(list(filter(lambda x: x <= arr[0], arr[1:]))) + arr[0:1] + qsort(list(filter(lambda x: x > arr[0], arr[1:]))) or arr
# #7、一行代码解决八皇后问题
# [__import__('sys').stdout.write('\n'.join('.' * i + 'Q' + '.' * (8-i-1) for i in vec) + "\n========\n") for vec in __import__('itertools').permutations(range(8)) if 8 == len(set(vec[i]+i for i in range(8))) == len(set(vec[i]-i for i in range(8)))]
#8、一行代码实现list, 有点类似与上个功能的反功能
# array = lambda x: [x[i:i+3] for i in range(0, len(x), 3)]
