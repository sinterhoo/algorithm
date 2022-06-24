

s = input()


if s[0] == '0':
    if len(s) > 1 and s[1] == 'x':
        print(int(s,16))
    else:
        print(int(s,8))
else:
    print(int(s))