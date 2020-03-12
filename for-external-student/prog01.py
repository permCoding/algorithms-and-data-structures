'''
    базовые алгоримические структуры
'''
def ex_01():
    a = '100'
    b = '99'
    if a>b:
        print(a)
    else:
        print(b)

def ex_02():
    s = '1234 5555'
    index_space = s.find(' ')
    print(s[:index_space])
    print(s[index_space+1:])

def ex_03():
    s = '1234 5555'
    lst = s.split(' ')
    print(lst[0])
    print(lst[1])

def ex_04():
    s = '123 555'
    lst = list(s)
    print(*lst)

def ex_05():
    s = '123 555'
    lst = list(s)
    for smb in lst:
        print(smb, end='')
    print()

def ex_06():
    s = '123 555'
    lst = list(s)
    for i in range(len(lst)-1, -1, -1):
        print(lst[i], end='')
    print()

def ex_07():
    s = '100 34 44 22 9 0'
    lst = s.split()
    print(sorted(lst))
    print(*sorted(lst))

def ex_08():
    s = '100 34 44 22 9 0'
    lst_string = s.split()
    lst_numbers = []
    for item in lst_string:
        lst_numbers.append(int(item))
    lst_numbers.sort()
    print(*lst_numbers)

def ex_09():
    s = '100 34 44 22 9 0'
    lst_string = s.split()
    lst_numbers = [int(item) for item in lst_string]
    lst_numbers.sort()
    print(*lst_numbers)

def ex_10():
    s = '100 34 44 22 9 0'
    lst_numbers = list(map(int, s.split()))
    print(*sorted(lst_numbers))

ex_10()
