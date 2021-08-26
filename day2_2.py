# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
i = 0
s = 0
n = 0
m = 0
while i < 10:
    n = input()
    n = int(n)
    if m < n:
        m = n
    s = s + n
    i += 1
p = s / i
print("最大的数：", m, '\n'"10个数的和：", s, '\n'"平均数：", '%d' % p)
