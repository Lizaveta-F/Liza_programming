s = input()
s1 = s.replace(' ', '')
place_eq = s1.find('=')
place_pl = s1.find('+')
place_x = s1.find('x')
if s1[0] == 'y':
    if s1[-1] == 'x':
        k = s1[place_pl+1:-1]
        b = s1[place_eq+1:place_pl]
    else:
        k = s1[place_eq+1:place_x]
        b = s1[place_pl+1:]
elif s1[-1] == 'y':
    if s1[-3] == 'x':
        b = s1[:place_pl]
        k = s1[place_pl+1:place_x]
    else:
        b = s1[place_pl+1:place_eq]
        k = s1[:place_x]
print("k =", k, "b =", b)
