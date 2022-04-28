import matplotlib.pyplot as plt
import random

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

y1 = []
y2 = []
y3 = []
a = 1000 / ((10000-4800)*(10000-4800)*(10000-4800))
b = 840

for x in range(0,10000,1000):
    r = random.uniform(-60.0,166.0)
    y1.append( (a*(x-4800)*(x-4800)*(x-4800) + b + r ))

for x in range(0,10000,1000):
    r = random.uniform(-60.0,166.0)
    y2.append( (a*(x-4800)*(x-4800)*(x-4800) + b + r ))

for x in range(0,10000,1000):
    r = random.uniform(-60.0,166.0)
    y3.append( (a*(x-4800)*(x-4800)*(x-4800) + b + r ))

plt.plot(range(0,10000,1000),y1,range(0,10000,1000),y2,range(0,10000,1000),y3)

plt.title("测试数据")
plt.xlabel("并发请求量")
plt.ylabel("延迟时间")
plt.savefig("fake_data.jpg")


print('hello')
