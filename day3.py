"""
    1.准备足够的金钱
    2.准备空的购物车
    3.商品有足够的商品
        容器技术
    4.开始购物
    5.结账
    6.打印购物小条
    技术选项：
        1.判断：if
        2.循环：while,for
        3.容器技术
            列表：
                增：append()
                删除：del 名称[角标]
                修改：名称[角标] = 新值
                查询：名称[角标]
        4.键盘输入:input
        5.打印print
    购物：
        是否存在商品：
            存在：
                钱是否足够：
                    够：
                        添加到我的购物车
                        余额减去相对应钱
                    不够：
                        温馨提示：穷鬼，对不起，钱不够，到其他地方买去！
            不存在：
                温馨提示：该物品不存在！别瞎弄！

    任务1：
        优化购物小条的打印操作，合并同类。
    任务2：
        10张机械革命优惠券，9折 2
        20张老干妈优惠券，1折 4
        15张辣条的优惠券，2折 3
    先随机抽取一张，最终结算的时候使用这个优惠券。
"""
import random

# 抽优惠券
print("欢迎光临本超市！本超市目前有抽奖活动，进店顾客可以抽取一张优惠券！")
input("按下回车即可参与抽奖！")
num = random.randint(1, 9)
if 0 < num < 3:
    print("恭喜这个比，获得机械革命9折优惠券")
    quan = 0
    zhe = float(0.9)
elif 2 < num < 7:
    print("恭喜这个比，获得老干妈1折优惠券")
    quan = 5
    zhe = float(0.1)
elif 6 < num < 10:
    print("恭喜这个比，获得辣条2折优惠券")
    quan = 6
    zhe = float(0.2)
# 1.准备商品
show = [
    ["机械革命", 9000],  # shop[chose][1]
    ["Think pad", 4500],
    ["Mac book pro", 12000],
    ["洗衣坟", 20],
    ["西瓜", 2],
    ["老干妈", 15],
    ["卫龙辣条", 3.5]
]
shop = [
    ["机械革命", 9000, 1],  # shop[chose][1]
    ["Think pad", 4500, 1],
    ["Mac book pro", 12000, 1],
    ["洗衣坟", 20, 1],
    ["西瓜", 2, 1],
    ["老干妈", 15, 1],
    ["卫龙辣条", 3.5, 1]
]
# 2.准备足够的钱
money = input("请输入初始余额：")
money = int(money)  # "5" --> 5

# 3.准备空的购物车
mycart = []

# 4.开始购物：

while True:  # 死循环
    # 展示商品
    for key, value in enumerate(show):
        print(key, value)

    # 输入
    chose = input("请输入您想要的商品编号：")
    if chose.isdigit():  # "5" --> 5
        chose = int(chose)
        # 商品是否存在
        if chose > len(shop):  # len()
            print("对不起，您输入商品不存在！别瞎弄！")
        else:
            # 金钱是否足够
            if chose == quan:
                qmoney = shop[chose][1] * zhe
                if money > qmoney:
                    mycart.append(shop[chose])
                    quan = -1
                    money = money - qmoney
                    print("恭喜，成功添加购物车!,优惠券已使用！您的余额还剩：￥%.2f" % money)
            else:
                if money < shop[chose][1]:
                    print("穷鬼，对不起，钱不够，到其他地方买去！")
                else:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
                    print("恭喜，成功添加购物车!,您的余额还剩：￥%.2f" % money)

    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！拜拜了您嘞！")
        break
    else:
        print("对不起，输入非法，请重新输入！别瞎弄！")

# 打印购物小条
mylist = []
for i in mycart:
    if i not in mylist:
        mylist.append(i)
    else:
        i[2] = i[2] + 1
print("以下是您的购物小条，请拿好：")
print("--------------Jason 商城------------------")
for key, value in enumerate(mylist):
    print(key, value)
print("您的钱包余额还剩：￥%.2f" % money)
print("-----------------------------------------")
