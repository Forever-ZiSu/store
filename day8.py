"""
分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体
"""


class Cup:
    __height = 0
    __volume = 0
    __colour = ""
    __stuff = ""

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def setVolume(self, volume):
        self.__volume = volume

    def getVolume(self):
        return self.__volume

    def setColour(self, colour):
        self.__colour = colour

    def getColour(self):
        return self.__colour

    def setStuff(self, stuff):
        self.__stuff = stuff

    def getStuff(self):
        return self.__stuff

    def liquid(self):
        print("这个高", self.__height, "cm，材质是", self.__stuff, "的", self.__colour, "杯子里存放了", self.__volume, "升的液体")


cup = Cup()
print("请输入杯子的高度：")
cup.setHeight(input())
print("请输入杯子的容积：")
cup.setVolume(input())
# print("请输入杯子的颜色：")
cup.setColour("黑色")
# print("请输入杯子的材质：")
cup.setStuff("陶瓷")
cup.liquid()


# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）


class Computer:
    __screen_size = 0
    __price = 0
    __cpu_model = ""
    __memory_size = 0
    __standby_time = 0

    def setScreen_size(self, screen_size):
        self.__screen_size = screen_size

    def getScreen_size(self):
        return self.__screen_size

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def setCpu_model(self, cpu_model):
        self.__cpu_model = cpu_model

    def getCpu_model(self):
        return self.__cpu_model

    def setMemory_size(self, memory_size):
        self.__memory_size = memory_size

    def getMemory_size(self):
        return self.__memory_size

    def setStandby_time(self, standby_time):
        self.__standby_time = standby_time

    def getStandby_time(self):
        return self.__standby_time

    def typing(self):
        print("你在使用一台价值", self.__price, "元，屏幕", self.__screen_size, "英寸", "CPU为", self.__cpu_model, "的",
              self.__memory_size, "GB内存", self.__standby_time, "小时待机时间的PC打字")

    def play_games(self):
        print("你在使用一台价值", self.__price, "元，屏幕", self.__screen_size, "英寸", "CPU为", self.__cpu_model, "的",
              self.__memory_size, "GB内存", self.__standby_time, "小时待机时间的PC打游戏")

    def watch_videos(self):
        print("你在使用一台价值", self.__price, "元，屏幕", self.__screen_size, "英寸", "CPU为", self.__cpu_model, "的",
              self.__memory_size, "GB内存", self.__standby_time, "小时待机时间的PC看视频")


pc = Computer()
print("请输入PC屏幕的尺寸：")
pc.setScreen_size(input())
print("请输入PC的价格：")
pc.setPrice(input())
print("请输入PC的CPU型号：")
pc.setCpu_model("i7-8550U")
print("请输入PC的内存大小：")
pc.setMemory_size(input())
print("请输入PC的待机时长：")
pc.setStandby_time(input())
pc.typing()
pc.play_games()
pc.watch_videos()
