age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"您需要交：{price}元")

# 判断一个变量num是否大于等于10
num = int(input("请输入一个数字:"))

if num >= 10:
    print("num大于等于10")
else:
    print("num小于10")

#判断一个字符串str是否等于"巢湖"
name=input("请输入一个名称:")
if name == "巢湖":
    print("名称叫巢湖")
else:
    print("名字不叫巢湖")

'''
如果用户输入了正确的用户名abcd以及对应的正确密码123456,则显示"登录成功"
若用户名或者密码有一个错了,都显示"用户名或密码错误"
'''

user_name = input("请输入账号:")
password = input("请输入密码:")
if user_name == "abcd" and password == "123456":
    print("登录成功")
else:
    print("用户名和密码错误")

'''
如果用户输入了正确的账号abcd和对应的正确密码123456,则显示"登录成功"
若用户名输入错误显示"账号错误",若密码错误则显示"密码错误"
若账号和密码都错误显示"账号和密码错误"
'''
user_name=input("请输入账号:")
password=input("请输入密码:")
if user_name=="abcd"and password=="123456":
    print("登录成功")
elif user_name!="abcd"and password=="123456":
    print("账号错误")
elif user_name == "abcd" and password != "123456":
    print("密码错误")
else:
    print("用户名和密码错误")

score = int(input("请输入考试成绩："))

if score >= 90:
    print("优秀")

else:
    if score >= 80:
        print("良好")
    else:
        if score >= 70:
            print("中等")
        else:
            if score >= 60:
                print("及格")
            else:
                print("不及格")

n=int(input())
print(n*(n+1)//2)

for i in range(10):
    print(i)

# 定义字符串
name = "itheima is a brand of itcast"
# 定义一个变量，用来统计有多少个a
count = 0
# for 循环遍历所有字母
# for 临时变量 in 被统计的数据:
for x in name:
    if x == "a":
    # 通过if判断变量是否等于a，等于a时count+1
        count += 1
print(f"被统计的字符串中有{count}个a")

for num in range(10,20):  # 迭代10到20之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)

      students = ["a", "b", "c"]
      for student in students:
          print(student)

