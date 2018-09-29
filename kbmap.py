kbmap = dict()
PLAIN = 0x0
SHIFT = 0x2

for i in range(26):
    kbmap[chr(97 + i)] = (4 + i, PLAIN)
    kbmap[chr(65 + i)] = (4 + i, SHIFT)
kbmap[' '] = (0x2C, PLAIN)
kbmap['='] = (0x2E, PLAIN)
for i in range(1, 10):
    kbmap[str(i)] = (0x1E + i - 1, PLAIN)
kbmap['0'] = (0x27, PLAIN)
for i, c in enumerate(")!@#$%^&*("):
    kbmap[c] = (kbmap[str(i)][0], SHIFT)
kbmap['/'] = (0x38, PLAIN)
kbmap['?'] = (0x38, SHIFT)
kbmap['\n'] = (0x28, PLAIN)

if __name__ == '__main__':
    for k in sorted(kbmap):
        print(k, " ".join(map(hex, kbmap[k])))

