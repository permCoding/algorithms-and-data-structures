class Convert():

    def __init__(self, par):
        if type(par) == int:
            self.dec = par
            self.bin = self.to_bin()
        else:
            self.bin = par
            self.dec = self.to_dec()

    def to_dec_rec(self, b):
        if b == '':
            return 0
        else:
            return self.to_dec_rec(b[:-1])*2 + int(b[-1])

    def to_bin_rec(self, d):
        if d == 0:
            return ''
        else:
            return self.to_bin_rec(d//2) + str(d%2)

    def to_dec(self):
        b = self.bin
        d = 0
        for i in range(len(b)):
            d += int(b[i]) * 2** (len(b)-1-i)  
        return d

    def to_bin(self):
        d = self.dec
        b = ''
        while d > 0:
            b = str(d%2) + b
            d //= 2
        return b

