#列表
    #define:由一系列按特定顺序排列的元素组成
    #列表通常包含多个元素，因此给列表指定一个表示复数的名称（如：letters，digits）
    #在python中，用[]表示列表，并用，分隔其中的元素
bicycles = ['trek','cannondale','redline']
print(bicycles)

#访问列表元素
    #列表是有序集合，要访问列表的任意元素，只需要将该元素的位置（索引）告诉python
bicycles = ['trek','cannondale','redline']
print(bicycles[1].title())
    #索引从0而不是从1开始
    #访问最后一个列表元素：索引指定为-1
bicycles = ['trek','cannondale','redline']
print(bicycles[-1].title())
    #使用列表中的各个值
message = f"my first bicycle was a {bicycles[-3]}."
print(message)

#练习
names = ['karrie','laurance','zzy','hurbet']
print(names[0].title())
print(names[1].title())
print(names[-1].title())
msg = "follow me to learn python."
print(f"Dear {names[0].title()}\n\t{msg}")

#修改、添加和删除元素
    #修改列表元素
        #可指定列表名和要修改的元素的索引，再指定该元素的新值
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
    #在列表中添加元素
        #在列表末尾添加元素
         #将元素附加（方法append（））到列表，给列表添加元素时，它将添加到列表末尾
motorcycles.append('honda')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('ducati')
motorcycles.append('suzuki')
print(motorcycles)
        #在列表中插入元素
         #使用方法insert()可在列表的任何位置添加新元素，为此需要指定新元素的索引和值
motorcycles.insert(0,'yamaha')
print(motorcycles)
        #从列表中删除元素
         #使用del语句删除元素（删除后，无法再访问删除的值）
del(motorcycles[0])
print(motorcycles)
del(motorcycles[1])
print(motorcycles)
del motorcycles[0]
print(motorcycles)
         #使用方法pop()删除元素
          #方法pop()删除列表末尾元素，并让你能够接着使用它。
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
         #弹出列表中任何位置处的元素
          #实际上，可以使用pop()来删除列表中任意位置的元素，只需在圆括号中指定要删除元素的索引
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"the first motorcycle i owned was a {first_owned.title()}.")
print(motorcycles)
         #根据值删除元素，remove()(从列表删除的元素，也可接着使用它的值)
          #注意：方法remove()只删除第一个指定值，如果删除的值在列表中出现多次，就需要使用循环来删除
motorcycles = ['honda','yamaha','suzuki','ducati','honda']
motorcycles.remove('ducati')
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"{too_expensive} is too expensive!")

#练习
invent_list = ['karrie','laurance','hurbet','jack']
print(f"{invent_list[0].title()} please come to dinner." )
print(f"{invent_list[1].title()} please come to dinner." )
print(f"{invent_list[2].title()} please come to dinner." )
print(f"{invent_list[3].title()} please come to dinner." )
print(f"{invent_list[3].title()} can not join dinner")
invent_list[3] = 'uzi'
print(f"{invent_list[0].title()} please come to dinner." )
print(f"{invent_list[1].title()} please come to dinner." )
print(f"{invent_list[2].title()} please come to dinner." )
print(f"{invent_list[3].title()} please come to dinner." )
print("because i found a bigger table , so i want to invent more friend to come to dinner")
invent_list.insert(0,'xiaohu')
invent_list.insert(3,'ming')
invent_list.append('nuguri')
print(f"{invent_list[0].title()} please come to dinner." )
print(f"{invent_list[1].title()} please come to dinner." )
print(f"{invent_list[2].title()} please come to dinner." )
print(f"{invent_list[3].title()} please come to dinner." )
print(f"{invent_list[4].title()} please come to dinner." )
print(f"{invent_list[5].title()} please come to dinner." )
print(f"{invent_list[6].title()} please come to dinner." )
print("i'm so sorry that i am only invent two friend to come to dinner beacause the table can not arrive in time.")
popped_invent_list = invent_list.pop()
print(f"{popped_invent_list.title()} i'm so sorry.")
popped_invent_list = invent_list.pop(-1)
print(f"{popped_invent_list.title()} i'm so sorry.")
popped_invent_list = invent_list.pop(-1)
print(f"{popped_invent_list.title()} i'm so sorry.")
popped_invent_list = invent_list.pop(-1)
print(f"{popped_invent_list.title()} i'm so sorry.")
popped_invent_list = invent_list.pop(0)
print(f"{popped_invent_list.title()} i'm so sorry.")
print(f"{invent_list[0].title()} please come to dinner." )
print(f"{invent_list[1].title()} please come to dinner." )
del invent_list[0]
del invent_list[0]
print(invent_list)

#组织列表
    #使用方法sort()对列表永久排序,按照字母顺序排序
cars = ['bmw','audi','toyota','byd']
cars.sort()
print(cars)
     #按照字母反向排序，向sort()方法传递参数 reverse = True即可（reverse：反向）
cars.sort(reverse = True)
print(cars)
    # 使用函数sorted()对列表临时排序
     #保留列表元素原来的排列顺序，同时按照特定顺序显示列表元素
cars = ['bmw','audi','toyota','byd']
print("here is the original list:")
print(cars)
print("\nhere is the sorted list:")
print(sorted(cars))
print("\nhere is the sorted reverse list:")
print(sorted(cars,reverse=True))
print("\nhere is the original list again:")
print(cars)
    #倒着打印列表
     #要反转列表元素的排列顺序，可以使用方法reverse()（永久排序，不过再次使用又会变回原本的顺序）
      #注意：reverse()方法不是按照字母顺序，而是反转列表元素
cars.reverse()
print(cars)
    #确定列表的长度
     #使用len()可以快速获取列表长度
      #注意：python计算列表元素数时是从1开始，因此不会遇到差1的错误
print(len(cars))

#练习
trip_adr = ['wuhan','sichuan','chongqin','hainan','hunan','beijing']
print(f"{trip_adr}\n")
print(f"{sorted(trip_adr)}\n")
print(f"{trip_adr}\n")
print(f"{sorted(trip_adr,reverse=True)}\n")
print(f"{trip_adr}\n")
trip_adr.reverse()
print(f"{trip_adr}\n")
trip_adr.reverse()
print(f"{trip_adr}\n")
trip_adr.sort()
print(f"{trip_adr}\n")
trip_adr.sort(reverse=True)
print(f"{trip_adr}\n")
print(len(invent_list))

#使用列表时避免索引错误
    #只有三个元素的情况下要求获取第四个元素
# trip_adr = ['wuhan','sichuan','chongqin']
# print(trip_adr[3])
    #发生索引错误却找不到办法时，可以尝试将列表或其长度打印出来。
