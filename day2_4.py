"""
从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
（结果判断：等腰，等边，直角，普通，不能形成三角形。）
"""
a, b, c = map(int, input("请输入三条边：\n如：3 4 5\n").split())
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("等边三角形")
    elif a == b or a == c or b == c:
        if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
            print("等腰直角三角形")
        else:
            print("等腰三角形")
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("直角三角形")
    else:
        print("普通三角形")
else:
    print("无法构成三角形")
