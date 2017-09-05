

def str():
    var1 = 'Hello World!'
    var2 = "Runoob"
    print("var1[0]: ", var1[0])
    print("var2[1:5):", var2[1:5])

    print("已更新字符串 ：", var1[:6] + 'Runoob!')

    a = "Hello"
    b = "Python"

    print("a + b 输出结果：", a + b)
    print("a * 2 输出结果：", a * 2)
    print("a[1]输出结果", a[1])
    print("a[1:4] 输出结果：", a[1:4])

    if ("H" in a):
        print("H 在变量 a中")
    else:
        print("H 不在变量 a 中")

    if("M" not in a):
        print("M 不在变量a 中")
    else:
        print("M 在变量a中")

    print(r'\n')
    print(R'\n')

    print("我叫 %s 今年 %d 岁." % ('小明', 12))

    para_str = """ 这是一个多行字符串的实力
	多行字符串可以使用制表符
	TAB(\t)。
	也可以使用换行符 [\n]。 """
    print(para_str)

    str = "23424234234"
    print("最大字符: " + min(str))

# str()


def _list():
    list1 = ['Google', 'Runoob', 1997, 2000]
    list2 = [1, 2, 3, 4, 5]
    list3 = ["a", "b", "c", "d"]

    print("list1[0]: ", list1[0])
    print("list2[1:5]: ", list2[1:5])

    print("第三个元素为： ", list1[2])
    list1[2] = 2001
    print("更新手第三个元素为： ", list1[2])

    print(len(list1))
    list4 = list1 + list2
    print(list4)
    print(["hi"] * 4)
    print(3 in list2)
    for x in list3:
        print(x, end=" ")
    print("\n")

    list5 = [list1, list2]
    print(list5)
    print(list5[0][1])

    # 列表中最大
    print(max(list2))
    # 列表中最小
    print(min(list2))

    # 元组转列表
    aTuple = (123, 'Google', 'Runoob', 'Taobao')
    list6 = list(aTuple)
    print("列表元素: ", list6)

    # 字符串转列表
    str = "Hello World"
    list_str = list(str)
    print("列表元素: ", list_str)

    list1.append("qjl")
    print("列表末尾添加后： ", list1)

    list_count = list1.count('Google')
    print("列表中o的个数：", list_count)

    list_extd = list(range(5))
    list1.extend(list_extd)
    print("扩展后的列表： ", list1)

    print('Runoob 索引值为', list1.index('Runoob'))
    print('Taobao 索引值为', list1.index(3))

    list1.insert(1, "Baidu")
    print('列表插入元素后为 ：', list1)

    list1.pop()
    print("列表现在为：", list1)
    list1.pop(1)
    print("列表现在为: ", list1)

    list1.remove(3)
    print("列表现在为： ", list1)
    list1.remove(0)
    print("列表现在为: ", list1)

    list1.reverse()
    print(list1)

    list_sort = list(range(50))
    print(list_sort)
    list_sort.sort()
    print("列表排序后： ", list_sort)
    print(list_sort[::-1])


# _list()

def tup():
    tup1 = ('Google', 'Runoob', 1997, 200)
    tup2 = (1, 2, 3, 4, 5)
    tup3 = "a", "b", "c", "d"
    tup4 = (range(10))

    print(tup4)

    print(tup1[0])
    print(min(tup2))

# tup()


def dict():
    dict = {'Name': 'qjl', 'Age': '30', 'Class': 'First'}
    print("dict[Nmae]:", dict['Name'])
    print("dict[Age]:", dict['Age'])
    dict['Name'] = 'qujl'
    print("更新后的dict[Name]:", dict['Name'])
    try:
        print("dict[Alice]:", dict[Alice])
    except Exception as e:
        print("dict[Alice]不存在")
    else:
        pass
    finally:
        print("我必须执行")

    dict["school"] = '菜鸟教学'
    print(dict['school'])

    # del dict["Name"]
    print(len(dict))
    # print (str(dict))

    # key in dict 判断键是不是在字典中
    if 'Age' in dict:
        print("键 Age 存在")
    else:
        print("不存在")

    if 'Sex' in dict:
        print("Sex存在")
    else:
        print("Sex不存在")

    # 字典 清除
    dict1 = {'Name': 'qjl', 'Age': '30', 'Class': 'First'}
    print("字典长度 ： %d" % len(dict1))
    dict1.clear()
    print("清楚后字典长度: %d" % len(dict1))

    # 字典的浅拷贝
    dict2 = dict.copy()
    print(dict2)

    dict3 = dict  # 浅拷贝：引用对象
    dict4 = dict.copy()  # 浅拷贝：深拷贝父对象(一级目录),子对象（二级目录）不拷贝，还是引用

    # 修改data数据
    dict['Name'] = 'root'
    del dict['Age']
    print(dict)
    print(dict3)
    print(dict4)

    # radiansdict.get(key,deault=None) 返回指定键的值，如果值不在字典中返回default值
    print("Age 值为 ： %s" % dict.get('Name'))
    print("Sex 值为 ： %s" % dict.get('Sex', 'Na'))

    # radiansdict.items() 以列表返回可遍历的（键，值）元组数组
    print("Value : %s" % dict.items())

    for i, j in dict.items():
        print(i, ":\t", j)

    print('Name' in dict)

    # 以列表返回一个字典的所有键
    print(dict.keys())

    # 以列表返回字典左右值
    print("以列表返回dict中的值：", list(dict.values()))

    # pop 删除给定的键key对应的值，返回值为被删除的值
    site = {'name': '荷叶茶', 'alexa': 10000, 'url': 'wwww.baidu.com'}
    pop_obj = site.pop('name')
    print(pop_obj)
    print(site)


dict()
