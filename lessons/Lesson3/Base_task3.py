N = int(input())
M = int(input())
L = int(input())
H = int(input())
if N > 0 and M > 0 and L > 0 and H > 0:
    first_line = "+"+("-"*L+"+")*M
    column = (("|"+" "*L)*M+'|\n')*H
    cell = first_line+'\n'+column
    print((cell)*N+first_line)
else:
    ("The input data is incorrect")
