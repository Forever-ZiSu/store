# 用循环来实现20以内的数的阶乘。（1!+2!+3!+……+20!）
i = 1
s = 0
n = 1
while i <= 20:
    n *= i
    s += n
    i += 1
print(s)
