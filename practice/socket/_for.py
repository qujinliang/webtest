

class _For_while(object):
    """docstring for _For_while"""

    def while_test(self, n):
        self.n = n
        self.sum = 0
        self.counter = 1
        while self.counter <= self.n:
            self.sum = self.sum + self.counter
            self.counter += 1
        return ("1 到 %d 之和为： %d" % (self.n, self.sum))

    def while_loop(self):
        try:
            self.var = 1
            while self.var == 1:
                self.num = int(input("输入一个数字 ： "))
                print("你输入的数字是： ", self.num)

        except ValueError:
            print("不能为空，请输入数字")
            self.while_loop()

        finally:
            print("Good bye!")

    def For_test(self):
        languages = ["C", "C++", "Perl", "Python"]
        for x in languages:
            print(x)

    def for_test02(self):
        sites = ["Baidu", "Google", "Runoob", "Taobao"]
        for site in sites:
            if site == "Runoob":
                print("菜鸟教程!")
                break
            print("循环数据" + site)
        else:
            print("没有循环数据！")
        print("完成循环！")

    def for_range(self):
        for x in range(1, 10, 3):
            print(x)
        for y in range(-10, -100, -30):
            print(y)

    def for_range_len(self):
        a = ['Google', 'Baidu', "Runoob", 'Taobao', 'QQ']
        for i in range(len(a)):
            print(i, a[i])

    def for_break(self):
        for letter in 'Runoob':
            if letter == 'b':
                break
            print('当前字母为：', letter)

        var = 10
        while var > 0:
            print('当前变量值为:', var)
            var = var - 1
            if var == 5:
                break
        print("Google bye!")

    def for_continue(self):
        for letter in 'Runoob':
            if letter == 'o':
                continue
            print('当前字母:', letter)

        var = 10
        while var > 0:
            var = var - 1
            if var == 5:
                continue
            print('当前变量值:', var)
        print("good bye!")

    def for_else(self):
        for n in range(2, 10):
            for x in range(2, n):
                if n % x == 0:
                    print(n, '等于', x, '*', n // x)
                    break
            else:
                print(n, '是质数')

    def for_pass(self):
        for letter in 'Runoob':
            if letter == 'o':
                pass
                print('执行pass块')
            print('当前字母', letter)

        print("Good bye!")

    def enumerate_test(self):
        sequence = [12, 34, 34, 23, 45, 76, 89]
        for i, j in enumerate(sequence):
            print(i, j)

    def sum_test(self):
        n = 0
        sum = 0
        for n in range(0, 101):
            sum += n
        return sum

    def chengfa99_test(self):
        i = 1
        while i <= 9:
            j = 1
            while j <= i:
                mut = j * i
                print("%d * %d = %d" % (j, i, mut), end=" ")
                j += 1
            print("")
            i += 1

    def for_test(self):
        for i in range(1, 9):
            for j in range(1, i + 1):
                print("*", end="")
            print("")

    def for_ex01(self):
        for i in range(1,6):
            name = input()
            print('第%s名 %s已领奖'%(i,name))


if __name__ == '__main__':
    num = _For_while()
    # print (num.while_test(10))
    # num.while_loop()
    # num.For_test()
    # num.for_test02()
    # num.for_range()
    # num.for_range_len()
    # num.for_break()
    # num.for_continue()
    # num.for_else()
    # num.for_pass()
    # num.enumerate_test()
    # print(num.sum_test())
    #num.chengfa99_test()
    # num.for_test()
    num.for_ex01()
