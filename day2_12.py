"""
继续完成上午的猜数字游戏的需求功能。
1.	添加计数打印功能
2.	添加次数金币功能和锁定系统功能。
"""
import random
num = random.randint(0, 100)
print(num)
i = 0
a = 0
while i < 100:
    a = input("请输入一个数字：\n")
    a = int(a)
    if a == num:
        i += 10
        print("你成功了！你猜了%d" % (i / 10), "次！")
        break
    elif a > num:
        i += 10
        print("你猜大了！你猜了%d" % (i / 10), "次！")
    else:
        i += 10
        print("你猜小了！你猜了%d" % (i / 10), "次！")
print("游戏结束！")
