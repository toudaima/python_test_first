# 逢七跳过
for num in range(0, 101):
    if (num > 10 and num % 10 == 7) or (num != 0 and num % 7 == 0):
        print("跳过：{}".format(num))