class Convert():

    def __init__(self, num_bin = '0'):
        self.num_bin = num_bin
        self.num_dec = ''

    def bin_to_dec(self):
        num_dec = 0
        for pos in range(len(self.num_bin)):
            # num_dec += int(num_bin[pos])*2**(len(num_bin)-1-pos)
            num_dec += int(self.num_bin[pos])*pow(2, len(self.num_bin)-1-pos)
        self.num_dec = num_dec

