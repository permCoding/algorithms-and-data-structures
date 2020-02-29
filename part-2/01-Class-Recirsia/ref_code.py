from module import Convert

num_bin = input()

obj = Convert(num_bin)
obj.bin_to_dec()

print(obj.num_dec)

print(obj.bin_to_dec_rec(num_bin))