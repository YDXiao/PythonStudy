import random

print("--这是我的第一个小游戏--")
ansnum = random.randint(1, 10)
count = 3
temp = input("不妨猜一下现在心里想的那个数字，你有"+str(count)+"次机会：")
guess = int(temp)
while guess != ansnum:
    count -= 1
    if guess > ansnum:
        print("大了大了")
    else:
        print("小了小了")
    if count >= 1:
        temp1 = input("猜错了，还有" + str(count) + "机会，再猜一下吧：")
        guess = int(temp1)
    else:
        print("机会用完了，结束了")
        break
else:
    print("你牛逼！")
    print("中了也没有奖励")
    
