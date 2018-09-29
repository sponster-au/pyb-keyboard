import pyb

i = 0
while True:
    pyb.LED(4).toggle()
    print("eric i = {}".format(i))
    i += 1
    pyb.delay(300)
