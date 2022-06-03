s = input()
count_lower = s.count('a')+s.count('b')+s.count('c')+s.count('d')+s.count('e')+s.count('f')+s.count('g')+s.count('h')+s.count('i')+s.count('j')+s.count('k')+s.count('l')+s.count(
    'm')+s.count('n')+s.count('o')+s.count('p')+s.count('q')+s.count('r')+s.count('s')+s.count('t')+s.count('u')+s.count('v')+s.count('w')+s.count('x')+s.count('y')+s.count('z')
count_upper = s.count('A')+s.count('B')+s.count('C')+s.count('D')+s.count('E')+s.count('F')+s.count('G')+s.count('H')+s.count('I')+s.count('J')+s.count('K')+s.count('L')+s.count(
    'M')+s.count('N')+s.count('O')+s.count('P')+s.count('Q')+s.count('R')+s.count('S')+s.count('T')+s.count('U')+s.count('V')+s.count('W')+s.count('X')+s.count('Y')+s.count('Z')
print(" The amount of upper case letters in the string is", count_upper)
print(" The amount of lower case letters in the string is", count_lower)
