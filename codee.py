def func(bonus, price):
    total = bonus / price
    n = 1
    while total > 0:
        total = total - n**2
        n = n + 1 
    while total == 0:
        print(n)
    if total < 0:
        print(n, total)

func(9,2)