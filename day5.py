import random

print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank = {}  # 创建一个空的字典
# 开户逻辑
bank_name = "狼腾测试猿银行"


# def chk_password(password):
#    if password == ip_password:


#                第一个对应第一个 不是名称对应名称
def bank_adduser(account, username, password, country, province, street, door):
    if len(bank) > 100:
        return 3
    if account in bank:  # 如变量在容器内执行下面的代码
        return 2
    bank[account] = {
        "username": username,  #
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": 0,
        "bank_name": bank_name
    }
    return 1


def adduser():  # 定义了一个方法
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    account = random.randint(10000000, 99999999)
    stast = bank_adduser(account, username, password, country, province, street, door)
    #        调用方法   （元素，，，，，，，，，）
    if stast == 3:
        print("你去别的银行吧")
    elif stast == 2:
        print("开户失败，你别重复")
    elif stast == 1:
        info = '''
                        ------------个人信息------------
                        用户名:%s
                        账号：%s
                        密码：******
                        国籍：%s
                        省份：%s
                        街道：%s
                        门牌号：%s
                        余额：%s
                        开户行名称：%s
                    '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))
        return 0


def deposit():
    account = input("请输入您要存款的账号：")
    account = int(account)
    if account in bank:
        money = input("请输入存款金额：")
        money = int(money)
        if money < 0:
            money = 0
        bank[account]["money"] = bank[account]["money"] + money
        print("存款成功！")
        return 0
    else:
        print("存款失败！")
        return 0


def cash():
    account = input("请输入您要取款的账号：")
    account = int(account)
    if account in bank:
        password = input("请输入您的密码：")
        #        password = int(password)
        if password in bank[account]["password"]:
            money = input("请输入取款金额：")
            money = int(money)
            if money < 0:
                money = 0
            if money <= bank[account]["money"]:
                bank[account]["money"] = bank[account]["money"] - money
                print("取款成功！")
                return 0
            else:
                print("取款失败！账户余额不足！")
                return 3
        else:
            print("密码错误！")
            return 2
    else:
        print("取款失败！")
        return 1

    # {'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1',
    # 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}


def transfer():
    account_out = input("请输入您要转出的账号：")
    account_out = int(account_out)
    account_in = input("请输入您要转入的账号：")
    account_in = int(account_in)
    if account_out and account_in in bank:
        password_out = input("请输入转出账号的密码：")
        #        password_out = int(password_out)
        if password_out in bank[account_out]["password"]:
            money = input("请输入转出金额：")
            money = int(money)
            if money < 0:
                money = 0
            if money <= bank[account_out]["money"]:
                bank[account_out]["money"] = bank[account_out]["money"] - money
                bank[account_in]["money"] = bank[account_in]["money"] + money
                print("转账成功！")
                return 0
            else:
                print("转账失败！转出账户余额不足！")
                return 3
        else:
            print("密码错误！")
            return 2
    else:
        print("转出或转入账号不存在！")
        return 1


def query():
    account = input("请输入您要查询的账号：")
    account = int(account)
    if account in bank:
        password = input("请输入您的密码：")
        #        password = int(password)
        if password in bank[account]["password"]:
            info = '''
                                        ------------个人信息------------
                                            用户名:%s
                                            账号：%s
                                            密码：%s
                                            国籍：%s
                                            省份：%s
                                            街道：%s
                                            门牌号：%s
                                            余额：%s
                                            开户行名称：%s
            '''
            print(info % (bank[account]["username"], account, bank[account]["password"],
                          bank[account]["country"], bank[account]["province"], bank[account]["street"],
                          bank[account]["door"], bank[account]["money"], bank[account]["bank_name"]))
            return 0
        else:
            print("密码错误！")
            return 0
    else:
        print("该用户不存在！")
        return 0


begin = input("请选择业务")
while True:
    if begin == "1":  # 您输入的业务等于1执行开户操作
        adduser()
        begin = input("开户成功！\n请选择业务：")
    elif begin == "2":
        deposit()
        begin = input("请选择业务：")
    elif begin == "3":
        cash()
        begin = input("请选择业务：")
    elif begin == "4":
        transfer()
        begin = input("请选择业务：")
    elif begin == "5":
        query()
        begin = input("请选择业务：")
    else:
        print(6, "、退出")
        break
