X, P, Y = int(input()), int(input()), int(input())
years = 0
while X <= Y:
    years += 1
    X = X+X*(P/100)
print(years)
