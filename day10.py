# from threading import Thread
import threading
import time

basket = 500
threadLock = threading.Lock()


class Producer(threading.Thread):
    count = 0

    def run(self) -> None:
        global basket
        while True:
            if basket < 500:
                threadLock.acquire()
                self.count = self.count + 1
                basket = basket + 1
                print("生产者，生产1个，已生产", self.count, "个，现在有", basket, "个")
                threadLock.release()
                time.sleep(0.1)
            else:
                time.sleep(3)
                if basket == 500:
                    print("无人来买，关门下班！")
                    break
        threadLock.release()


class Consumer(threading.Thread):
    count = 0
    money = 3000

    def run(self) -> None:
        global basket
        while True:
            if self.money > 0:
                if basket > 0:
                    self.money = self.money - 2
                    self.count = self.count + 1
                    threadLock.acquire()
                    basket = basket - 1
                    print("消费者，购买1个，已购买", self.count, "个，现在有", basket, "个,钱还剩", self.money, "元")
                    threadLock.release()
                    time.sleep(0.1)
                else:
                    time.sleep(2)
            else:
                print("爷没钱了！溜了溜了！")
                break


p1 = Producer()
p2 = Producer()
p3 = Producer()
c1 = Consumer()
c2 = Consumer()
c3 = Consumer()
c4 = Consumer()
c5 = Consumer()
c6 = Consumer()
p1.start()
p2.start()
p3.start()
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
