N = int(input())
amount_tail = 0
amount_eagle = 0
for _ in range(N):
    coin = int(input())
    if coin == 1:
        amount_tail += 1
    else:
        amount_eagle += 1
if amount_tail < amount_eagle:
    print("The amount of returns = ", amount_tail)
else:
    print("The amount of returns = ", amount_eagle)
