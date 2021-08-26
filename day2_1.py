# 实现输入10个数字，并打印10个数的求和结果
i = 0
s = 0
n = 0
while i < 10:
    n = input()
    n = int(n)
    s = s + n
    i += 1
print(s)
