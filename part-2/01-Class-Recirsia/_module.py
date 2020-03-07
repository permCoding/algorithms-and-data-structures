class Convert():

    def to_dec_rec(self, b):
        if b == '':
            return 0
        else:
            return self.to_dec_rec(b[:-1])*2 + int(b[-1])

    def to_dec(self, b):
        d = 0
        for i in range(len(b)):
            d += int(b[i]) * 2** (len(b)-1-i)  
        return d

    def to_bin(self, d):
        b = ''
        while d > 0:
            b = str(d%2) + b
            d //= 2
        return b

    def to_bin_rec(self):
        return '110'
