# 使用while循环实现99乘法表的打印。
x = int(1)
y = int(1)
while x:
    while y:
        print(x, "*", y, "=", x * y)
        y = y + 1
        if y > 9:
            y = 1
            break
    x = x + 1
    if x > 9:
        break
