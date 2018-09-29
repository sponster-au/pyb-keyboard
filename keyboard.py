import pyb

from kbmap import kbmap

kb = pyb.USB_HID()
buf = bytearray(8)


def sendchr(char):
    if char not in kbmap:
        char = "?"
    # key down
    buf[2], buf[0] = kbmap[char]
    kb.send(buf)
    pyb.delay(15)
    # key up
    buf[2], buf[0] = 0x00, 0x00
    kb.send(buf)
    pyb.delay(15)


def sendstr(s):
    for c in s:
        sendchr(c)


# pyb.delay(5 * 1000)
x = 0
while True:
    s = "# experiment USB keyboard X = {} {}\n".format(x, hex(x))
    print(s)
    # pyb.LED(4).toggle()
    pyb.LED(3).toggle()
    sendstr(s)
    x += 1
    pyb.delay(1000)
