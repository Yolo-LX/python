print("\t\t静夜思")
print("\t\t\t李白")
print("床前明月光,", end =" ")
print("疑是地上霜.")
print("举头望明月,", end = " ")
print("低头思故乡，")
# end = ''是print()的一个参数。
# 作用：为end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串。
print("床前明月光,")
print("疑是地上霜.")
print("举头望明月,")
print("低头思故乡，")
 # 		静夜思
# 			李白
# 床前明月光, 疑是地上霜.
# 举头望明月, 低头思故乡，
# 床前明月光,
# 疑是地上霜.
# 举头望明月,
# 低头思故乡，
# python的print()函数中参数end=’ ‘默认为\n，所以会自动换行。
# 默认的print()函数：
# print(end=’\n’)
 # 解决
# 把参数end=’ ‘设置成你想要的就行了，如end=’’，那么它就是以结尾
#考点： end    print的功能



# name =  Anny    NameError: name 'Anny' is not defined. Did you mean: 'any'?
name = "Anny" #字符串变量
age = 5 #整形变量
age = 4.5  #整形变量
school = 'kindergarden' #字符串变量
print(f"{name} is {age} years old, she is in {school}.")#Anny is 4.5  ears old, she is in kindergarden.
print("%s is  %d years old, she is in  %s."%(name,age,school))# Anny is  4 years old, she is in  kindergarden.
         #Anny is 5 years old, she is in kindergarden.
# 在python中没有字符常量和变量的概念,只有字符串类型的常量和变量,使用单引号,双引号,三双引号作为定界符.
#  print语句中加入f就可以起到和format函数（格式化）  相的作用。格式：print(f'{表达式}')格式：print(f'{表达式}')
#%求余数，字符格式化//p15
# 考点：对变量的创建
# 字符格式化的理解





import time#倒入奶标准库time
t1 = time.localtime()#模块名
t2 = time.localtime()
t3 = time.localtime()
print(t1)#time.struct_time(tm_year=2023, tm_mon=3, tm_mday=4, tm_hour=11, tm_min=17, tm_sec=27, tm_wday=5, tm_yday=63, tm_isdst=0)
print(t2)#time.struct_time(tm_year=2023, tm_mon=3, tm_mday=4, tm_hour=11, tm_min=17, tm_sec=27, tm_wday=5, tm_yday=63, tm_isdst=0)
print(id(t1))#3041349497792
print(id(t2))#3041349495104
print(id(t3))#3041349495104
print(t1 == t2)#True
print(t1 is t2)#False
# #struct tm {
#    int tm_sec;         /* 秒，范围从 0 到 59                */
#    int tm_min;         /* 分，范围从 0 到 59                */
#    int tm_hour;        /* 小时，范围从 0 到 23                */
#    int tm_mday;        /* 一月中的第几天，范围从 1 到 31                    */
#    int tm_mon;         /* 月份，范围从 0 到 11                */
#    int tm_year;        /* 自 1900 起的年数                */
#    int tm_wday;        /* 一周中的第几天，范围从 0 到 6                */
#    int tm_yday;        /* 一年中的第几天，范围从 0 到 365                    */
#    int tm_isdst;       /* 夏令时                        */
# };
# 考点：Python time localtime() 函数类似gmtime()，作用是格式化时间戳为本地的时间。 如果sec参数未输入，则以当前时间为转换标准。 DST (Daylight Savings Time) flag (-1, 0 or 1) 是否是夏令时。
#为什么t1和t2不相等


