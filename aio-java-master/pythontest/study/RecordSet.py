# 常规了解
def baseInfo():
    # 输入输出 # 格式化输出
    a = int(input("输入一个int类型参数:"))
    print("输出换行(用逗号，没有换行符)", "这是第二行")
    print("输出int型参数:{%i}" % a)
    print("输出布尔型参数:{%r}" % 5 > 4 and 6 > 5)
    print("%")
    # {%x}{%X}带符号的十六进制，大小写
    # {%o}带符号的八进制
    # {%f}{%F}十进制浮点数
    # {%e}{%E}科学计数法浮点数，大小写

    # \ 反斜杠用于代码过长换行
    print("反斜杠换\
        行")
    a = 68
    b = 123.51434132
    print("a的值是十进制={%8d};八进制={%8o};十六进制={%8x}" % (a, a, a))
    print("b的值是小数{%f},科学计数={%e}" % (b, b))
    print("a的值左对齐和右对齐{%8d}，{%-8d}" % (a, a))
    print("b的值是宽度和小数位数{%16f}{%.2f}{%16.2f}" % (b, b, b))


# 数据类型
def dataType():
    # 整型标识范围几乎无限
    # 十进制 不已0开头的数字
    print(123)
    # 二进制 以0b或0B开始的数字
    print(0b1011)
    # 八进制 以0o或0O开始的数字
    print(0o1234)
    # 十六进制 0x或0X开始的数字
    print(0x1AF3)

    # 浮点型
    # 小数表示
    print(1.234)
    # 科学计数法
    print(1.234e3)

    # 布尔类型
    # true是1  false是0 ； true + 1结果是3
    # 以下输出为false
    if 0: print("false")
    if "": print("false")
    if None: print("false")
    if []: print("false")
    if (): print("false")
    if {}: print("false")

    # 字符
    # （了解ASCII码表）：A-65，a-97 1-49，=-61（字符-ASCII位置）
    print(chr(65))
    print(chr(97))
    print(chr(49))
    print(chr(61))
    print(ord("A"))
    # 一个中文需要16位二进制数（2个字节）表示
    # 字符串从0开始计数,字符串切割
    print("Python"[2:5])
    print("Python"[:3])
    # 转义字符\
    print("It\'s me 用引号\",TAB:\t,")
    print('  \\"。单引号:\\\'')

    # 前缀 u,r,b
    # u:表示字符串是一个Unicode编码，用于中日韩文，python3之后就不需要区别了
    str1 = u"中文"
    # r:表示字符串是一个原始的字符串，及不考虑字符串中的转义字符
    str = r"it\'s python"  # 结果打印的是it\'s python
    # b:表示二进制串，不支持中文，也不存在转义字符的概念
    a = b"text"
    print("%s" % a)  # b'text'
    print(type(a))  # <class 'bytes'>
    abc0 = a.decode("utf-8")
    print("%s" % abc0)  # text
    print(type(abc0))  # <class 'str'>

    # 字符串运算
    # +：拼接字符串，*：重复输出，[n]:输出索引所在的字符，[n,m]:截取字符串起始位置
    # in:判断是否存在（'He' in "Hello"）,not in:判断不存在，
    # 字符串常用方法：https: // www.runoob.com / python / python - strings.html

    # 数据类型转换
    print(str(123))
    print("字符串转int:{%i}" % int("123"))
    print("字符串转八进制int:{%i}" % int("123", 8))
    print("转浮点:{%f}" % float("1.1223"))
    print("转布尔:{%r}" % bool({}))
    # bin()转二进制，oct()转八进制，hex()转十六进制


def operator():
    a = 13
    b = "A"
    print("这个数是否是奇数：{%r}" % (a % 2 != 0))
    print("这个数是否是小写字母：{%r}" % (b >= 'a' and b <= 'z'))
    print("判断这个字符是不是")


def listRe():
    print("列表List")
    list1 = [1, 2, 4, 5, 3, 76, 34, 324, 3]
    # 遍历
    # 第一种：索引遍历
    for i in range(len(list1)):
        print(list1[i])
    # 第二种：元素遍历
    for item in list1:
        print(item)
    # 第三种：同时访问索引和元素
    list2 = [1, 2, 4, 2, "cd", 76, 34, 324, 3]
    for i, item in enumerate(list1):
        print("第", i, "条=", item)

    # 常用方法
    list1.append(11)  # 列表末尾添加
    list1.insert(2, 11)  # 列表中间添加
    # d = list1.pop(x)#删除x位置的数据，x为复数从末尾往前数，有返回删除的数据
    # list1.remove(obj)#删除列表第一个符合的元素
    # list1.count(2) #结果是2，计数
    # list1.index(2) #1 查找位置
    # list1.sort()#排序，所有数据类型要么都是字符串，要么都是数字.  sorted(list1)排序返回list，原来的list1数据不变
    # range(初值，限值，步长)#随机生成一系列数字
    # 列表解析 例如：list0 = [i*i for i in range(1,11)]


def douhao():
    # 分隔符
    a, b = 1, 2
    print(a, b)
    # 输出为一行
    list1 = [1, 2, 4, 5, "cd", 76, 34, 324, 3]
    for i, item in enumerate(list1):
        print("第", i, "条=", item)
    # 将变量或者参数转换成元组
    a = 1
    b = a,
    print(a)
    print(b)


def tupleRe():
    # 元组的值不可变
    # 创建元组用的是()，列表是[]
    tuple1 = (1, 2, 'A', "a")
    # 只要不改变值，其他操作和列表一样


def programMe(index):
    # if判断：可以多层嵌套，判断语句用括号，或|| ，&&且
    if ("aa".__eq__("aa")):
        print("相等")
    elif ("bb".__eq__("bb")):
        print("相等")
        if 1 > 0:
            print("1>0")
        else:
            print("不相等")
    else:
        print("不相等")
    #python 没有switch语句，if已经可以替代了
    switch={
        1:
            print(""),
        default:
            print(""),
    }

    #while循环
    i=2
    while i<6:
        print("index is {%i}"%i)

    str = 'hello'
    for i in str:
        print(i)


