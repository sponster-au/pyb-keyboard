import pyb

dx = 1
x = 0

led = pyb.LED(4)
while True:
    led.intensity(x)
    # pyb.LED(2).toggle()
    pyb.LED(3).intensity(255 - x)
    x += dx
    if x == 255:
        dx = -1
    if x == 0:
        dx = 1
    pyb.delay(5)
