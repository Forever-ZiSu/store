"""
有以下两个数，使用+，-号实现两个数的调换。
A=56
B=78
实现效果：
A=78
B=56
"""
A = 56
B = 78
print("A=", A, "B=", B)
A = A + B
B = A - B
A = A - B
print("A=", A, "B=", B)
