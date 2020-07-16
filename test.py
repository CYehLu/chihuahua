from time import sleep
from chihuahua import chihuahua

@chihuahua(background='black')
def test1(a, b):
    return a + b

@chihuahua(background='black', rotate=True)
def test2(a, b):
    return a + b


print(' ==== test chihuahua ====')
print('func test1: one chihuahua')
test1(1, 2)
sleep(2)

print('func test2: rotated chihuahua')
test2(1, 2)