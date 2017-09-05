def dog_age():
    age = int(input("请输入你家狗狗的年龄："))
    print("")
    if age < 0:
        print("你特么在逗我吧!?")
    elif age == 1:
        print("相当于 14 岁的人")
    elif age == 2:
        print("相当于 22 岁的人")
    elif age > 2:
        human = 22 + (age - 2) * 5
        print("对应人类年龄： ", human)

        # 退出提示
    input("点击 enter 键退出")


def shili01():
    # 演示 ==操作符
    # 使用数字
    print(5 == 6)
    # 使用变量
    x = 5
    y = 8
    print(x == y)

# shili01()

# 该实力演示了数字猜谜游戏
import random


def high_low():
    number = random.randint(0, 100)
    guess = -1
    print("数字猜谜游戏")
    while guess != number:
        guess = int(input("请输入你猜的数字: "))

        if guess == number:
            print("真牛逼，猜对了！")
            print("就是:", number)
        elif guess < number:
            print("垃圾猜小了。。。继续")
        elif guess > number:
            print("垃圾猜大了。。。继续")

# high_low()


def test_if():
    num = int(input("输入一个数字："))
    if num % 2 == 0:
        if num % 3 == 0:
            print("你输入的数字可以整除2和3")
        else:
            print("你输入的数字可以整除,但不能整除3")

    else:
        if num % 3 == 0:
            print("你输入的数字可以整除3,但不能整除2")
        else:
            print("你输入的数字不能整除 2 和 3")
# test_if()


def if_random():
    x = random.choice(range(100))
    y = random.choice(range(200))

    if x > y:
        print('x:', x)
    elif x == y:
        print('x+y', x + y)
    else:
        print('y:', y)

# if_random()


def dog_age2():
    print("============欢迎进入狗狗年龄对比系统============")
    while True:
        try:
            age = int(input("请输入你家狗的年龄："))
            print(" ")
            age = float(age)
            if age < 0:
                print("你特么在逗我？？")
            elif age == 1:
                print("相当于人类14岁")
                break
            elif age == 2:
                print("相当于人类22岁")
                break
            else:
                human = 22 + (age - 2) * 5
                print("相当于人类：", human)
                break
        except ValueError:
            print("输入不合法，请输入有效年龄")

    # 退出提示
    input("点击enter键退出")
dog_age2()
