"""f = open("layer0", 'r')
s = ""
for line in f.readlines():
    for c in line:
        if c == 'g':
            s += '00'
        elif c == 'f':
            s += '01'
        elif c == 's':
            s += '02'
        elif c == 'h':
            s += '03'
        elif c == 'i':
            s += '04'
        elif c == 'j':
            s += '05'
        elif c == 'k':
            s += '06'
        elif c == 'l':
            s += '07'
        elif c == 'm':
            s += '14'
        elif c == 'n':
            s += '15'
        elif c == 'o':
            s += '22'
        elif c == 'p':
            s += '23'
        elif c == 't':
            s += '08'
        elif c == '\n':
            s += ''
        else:
            s += 'NN'
        s += ' '
    s += '\n'

print(s)"""


class A:
    def _f2(self):
        pass

    def f1(self):
        print("salut")
        self._f2()


class B(A):
    def _f2(self):
        print("à tous")


b = B()
b.f1()