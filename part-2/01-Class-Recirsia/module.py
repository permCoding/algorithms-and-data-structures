class Convert():

    def __init__(self, num_bin = '0'):
        self.num_bin = num_bin
        self.num_dec = '0'

    def bin_to_dec(self):
        num_dec = 0
        for pos in range(len(self.num_bin)):
            # num_dec += int(num_bin[pos])*2**(len(num_bin)-1-pos)
            num_dec += int(self.num_bin[pos])*pow(2, len(self.num_bin)-1-pos)
        self.num_dec = num_dec

    # def bin_to_dec_rec(self, b):
    #     # return 0 if len(b) == 0 else int(b[0])*pow(2, len(b)-1) + self.bin_to_dec_rec(b[1:])
    #     if len(b) == 0:
    #         return 0
    #     else:
    #         return int(b[0])*pow(2, len(b)-1) + self.bin_to_dec_rec(b[1:])
        
    def bin_to_dec_rec(self, b):
        if len(b) == 0:
            return 0
        else:
            return int(b[-1]) + 2 * (self.bin_to_dec_rec(b[:-1]))
    
class Multi():

    def __init__(self, par = 'd', num = '0'):
        if par == 'b':
            self.num_bin = str(num)
            self.num_dec = self.bin_to_dec_rec(self.num_bin)
        elif par == 'd':
            self.num_dec = int(num)
            self.num_bin = self.dec_to_bin_rec(self.num_dec)
        else:
            self.num_bin = '0'
            self.num_dec = '0'

    def bin_to_dec_rec(self, b):
        if len(b) == 0:
            return 0
        else:
            return int(b[-1]) + 2 * (self.bin_to_dec_rec(b[:-1]))

    def dec_to_bin_rec(self, b):
        '''
            рекурсивный метод перевода из 10-ой в 2-ую
        '''
        return '1101000'