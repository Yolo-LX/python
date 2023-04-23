def getpass_state(pwd): # 定义一个函数名为getpass_state的函数并传参
    count_all = len(pwd) # 长度
    count_upper = 0 # 大写
    count_lower = 0 # 小写
    count_digit = 0 # 数字
    for char in pwd:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char.isdigit():
            count_digit += 1
    return (count_all, count_upper, count_lower, count_digit)
def resultout():
    call, cupper, clower, cdigit = getpass_state(password)
    print('密码长度为{}'.format(call))#格式化
    print('密码内大写字母有{}个'.format(cupper))
    print('密码内小写字母有{}个'.format(clower))
    print('密码内数字有{}个'.format(cdigit))
password = input("请输入密码:") # 1
resultout() # 调用函数
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
# 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号 : 起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。

# 定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。
# 这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。
# 要求：
# 1. 阅读并运行程序，结合函数一章的基础知识，给程序语句添加注释，说明程序的功能；
# 2. 分析程序，找到程序中的知识要点；
# 3. 总结函数的声明、调用等基本用法

# def main(n):
#     start = 10 ** (n - 1) #  #待测试数范围的起点和结束值
#     end = 10 ** n #参数n表示数字的位数，例如n=3时返回495，n=4时返回6174
#     for i in range(start, end): # 100-999   #由这几个数字组成的最大数和最小数
#       #将字符串中的每个成员以字符','分隔开再拼接成一个字符串；sort简单的升序排列 ，reverse=True：倒序；
#         big = ''.join(sorted(str(i), reverse=True))
#         little = ''.join(reversed(big))
#         big, little = map(int, (big, little))
#         if big - little == i:
#             print(i)
#
# main(1) #调用传参
def main(n):
    '''参数n表示数字的位数，例如n=3时返回495，n=4时返回6174'''
    #待测试数范围的起点和结束值
    start = 10**(n-1)
    end = 10**n
    #依次测试每个数
    for i in range(start, end):
        #由这几个数字组成的最大数和最小数
        big = ''.join(sorted(str(i),reverse=True))
        little = ''.join(reversed(big))
        big, little = map(int,(big, little))
        if big-little == i:
            print(i)
main(4)
# 要求：
# 1. 阅读程序，给程序语句做注释，掌握所涉及函数的用法；
# 2. 运行程序，找到程序的错误，分析错误原因，并对程序进行修改；
# 3. 自定义一个函数，实现：接收用户输入的数字 n（黑洞数的位数），输出 n
# 位数的黑洞数及该黑洞数的各数位数字所组成的最大数和最小数