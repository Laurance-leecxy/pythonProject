#第一个程序
print("hello python world!")
print("输入错误")

#变量:是可以赋给值的标签/指向特定的值
message = "hello python world"
print(message)
    #每一个变量都指向一个值
message = "hello python crash course world!"
print(message)
    #在程序中可随时修改变量的值，而，python将始终记录变量的最新值

#变量的命名及使用
    # 变量名的组成：字母 数字 下划线
    #     不可以数字打头，不能包含空格
    #         message_1 √  1_message ×
    #         greeting_message √  greeting message ×
    #     python中的关键字及函数名不可用作变量名
    #     慎用小写字母l和大写字母O
# message = "hello python crash course reader"
# print(mesage)

#练习：
simple_message = "一条简单消息"
print(simple_message)
simple_message = "两条简单消息"
print(simple_message)

#字符串：一系列字符
msg = 'i told my friend, "python is my favorite language"'
print(msg)
msg = "the language 'python' is named after monty python, not the snake."
print(msg)

#使用方法修改字符串大小写
name = "ada lovelace"
print(name.title())
#方法：是python可对数据执行的操作
print(name.upper())
print(name.lower())

#在字符串中使用变量
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"hello,{full_name.title()}!")
print(full_name.title())
#要在字符串中插入变量的值，可在前引号前加上字母f，再将要插入的变量放在花括号内。
#当python显示字符串时，将把每个变量都换成其值。
#这种字符串名为f字符串。f是format（设置格式）的简写
print("{}{}{}".format("hell0,",full_name,"!"))

#使用制表符或换行符来添加空白
#空白泛指任何非打印字符，如空格，制表符，换行符
    #添加制表符：\t
print("python")
print("\tpython")
    #添加换行符：\n
print("languages:\npython\nc\njavascript")
print("languages:\n\tpython\n\tc\n\tjavascript")

#删除空白
#python能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白，可使用方法rstrip（）
favorite_language = "python "
print(favorite_language.rstrip())
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
#剔除字符串开头的空白：lstrip（）；剔除开头末尾的空白：strip（）
favorite_language = " python "
print(favorite_language.lstrip())
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)


#使用字符串时避免语法错误
    #在用单引号括起的字符串中，如果包含撇号，就将导致错误
msg = "python's strength"
print(msg)
# msg = 'python's strength'
# print(msg)
msg = "python is a “language” very nice"
print(msg)
# msg = "python is a "language" very nice"
# print(msg)

#练习
name = "Eric"
print(f"hello {name},would you like to learn some python today")
name = "laurance.leE"
print(name.title())
print(name.lower())
print(name.upper())
print("\tAlbert Einstein once said,“A person who never made a mistake\nnever tried anything new.” ")
famous_person = "Albert Einstein"
message = "A person who never made a mistake\nnever tried anything new."
full_msg = f"\t{famous_person} once said,“{message}“"
print(full_msg)
name = "  msg\n\tname:laurance.lee\n\tage:25  "
print(name.strip())

#整数
    #可对整数执行+ - * / 运算
    #两个乘号表示幂运算
    #支持运算次序，可在同一表达式中使用多种运算符，，可使用圆括号修改运算次序
    #空格不影响python计算表达式的方式
#浮点数
    #所有带小数点的数称为浮点数。
    #注意：结果包含的小数位数可能是不确定的
    #如：0.2+0.1 = 0.300000000004
#整数&浮点数
    #将任意两个数相除时，结果总是浮点数（即便这两个数都是整数且能整除）
    #在其他任何运算中，如果一个操作数是整数，另外一个操作数是浮点数，结果也总是浮点数
#数中的下划线
    #书写很大的数时，可使用下划线将其中的数字分组，使其更清晰易读
        #打印使用下划线定义的数时，python不会打印其中的下划线
universe_age = 14_000_000_000
print(universe_age)
#同时给多个变量赋值
    #链式赋值
x = y = 1
print(x)
print(y)
    #系列解包赋值
x,y,z = 1,2,3
print(x)
print(y)
print(z)
#常量
    #常量类似于变量，但其值在程序的整个生命周期内保持不变。
    #python没有内置的常量类型
    #python程序员会使用全写大写来指出应将某个变量视为常量
MAX_CONNECTIONS = 5000
    #△在代码中，要指出应将特定的变量视为常量，可将其字母全部大写

#练习
print(4+4)
print(9-1)
print(2*4)
print(2**3)
print(16/2)
SUKIBANGOU = 1017
print(f"favorite number is {SUKIBANGOU}")

#注释
    #能够使用自然语言在程序中添加说明
    #注释用井号（#）
#该编写什么样的注释
    #目的：阐释代码要做什么，及如何做

