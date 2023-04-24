def xutianjie():
    raw_data = input('请输入密码：')

    num_asc = 0  # ASCII累加值

    str_pwd = ''  # ASCII拼接值

    for i in raw_data:
        ascii_val = ord(i)  # 1.获取每个元素的ASCII值

        num_asc = ascii_val + num_asc  # 2.对遍历的ASCII值进行累加操作

        str_pwd += str(ascii_val)  # 3.拼接操作

        reversal_num = str_pwd[::-1]  # 4.将拼接的ASCII值倒序排列

        encryption_num = int(reversal_num) + num_asc

    print(f"加密后的密码为：{encryption_num}")
xutianjie()
# 首先使用input()函数接收用户的输入的密码，之后设定变量num_asc与变量str_pwd分别来表示数字ASCII累加值与数字ASCII拼接值，
# 然后在for循环中遍历用户输入的密码，使用ord()函数获取每个数字元素的ASCII值并赋值给变量ascii_val，累加所有的ASCII值并赋值给变量num_asc，对每个数字的ASCII值对进行拼接操作并赋值给变量str_pwd，
# 通过切片方式将拼接后的结果进行倒序排列，最后将变量num_asc和变量reversal_num进行累加并赋值给变量encryption_num。