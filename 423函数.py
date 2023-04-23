def getpass_state(pwd):
    count_all = len(pwd)
    count_upper = 0
    count_lower = 0
    count_digit = 0
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
    print('密码长度维{}'.format(call))
    print('密码内大写字母有{}个'.format(cupper))
    print('密码内小写字母有{}个'.format(clower))
    print('密码内数字有{}个'.format(cdigit))
password = input("请输入密码:")
resultout()
# 要求：
# 1. 阅读并运行程序，结合函数一章的基础知识，给程序语句添加注释，说明程
# 序的功能；
# 2. 分析程序，找到程序中的知识要点；
# 3. 总结函数的声明、调用等基本用法

def main(n):
    start = 10 ** (n - 1)
    end = 10 ** n
    for i in range(start, end):
        big = ''.join(sorted(str(i), reverse=True))
        little = ''.join(reversed(big))
        big, little = map(int, (big, little))
        if big - little == i:
            print(i)
main(3)
print(big,little)
要求：
# 1. 阅读程序，给程序语句做注释，掌握所涉及函数的用法；
# 2. 运行程序，找到程序的错误，分析错误原因，并对程序进行修改；
# 3. 自定义一个函数，实现：接收用户输入的数字 n（黑洞数的位数），输出 n
# 位数的黑洞数及该黑洞数的各数位数字所组成的最大数和最小数