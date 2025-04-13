'''
name = "xxx"
score = 90
Student_ID = 123456
message = "我是：%s,我考了：%d,我的学号是：%f" % (name,score,Student_ID)
print(message)
'''


l = [6, 5, 4, 3, 2, 1]
for i in range(0, len(l) - 1):  # 0,4
    for j in range(i + 1, len(l)):  # 1,5
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print(l)