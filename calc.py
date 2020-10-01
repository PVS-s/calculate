with open('*.txt', 'r') as file:
    num = [float(z) for z in (z.strip() for z in file) if z]

av = sum(num) / len(num)
sd = (sum((n - av) ** 2 for n in num) / len(num)) ** .5
print("The arithm mean's {}".format(av))
print("The stand. deviation's {}".format(sd))
print("The min's {}.".format(min(num)))
