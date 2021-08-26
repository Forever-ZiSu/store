# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
username = "root"
password = "admin"
i = 3
while i > 0:
    user = input("用户名：\n")
    while i > 0:
        user_password = input("密码：\n")
        if user == username and user_password == password:
            i = 0
            print("登陆成功！")
        elif user == username and i > 1:
            i -= 1
            print("登陆失败！密码错误！你还剩", i, "次机会！请重新输入！")
        elif user == username and i == 1:
            i -= 1
            input("登陆失败！密码错误！系统已锁定！")
            i -= 1
        else:
            print("登陆失败！该用户不存在！请重新输入！")
            break
while i == -1:
    input("密码错误次数已超过三次！系统已锁定！")
