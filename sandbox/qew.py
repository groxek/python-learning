for n in range(1, 100000000):
    dv = bin(n)[2:]
    if n % 5 == 0:
        dv += str(bin(5)[2:])
    else:
        dv += "1"

    if int(dv,2) % 7 == 0:
        dv += str(bin(7)[2:])
    else:
        dv += "1"

    R = int(dv, 2)
    if R < 1_855_663:
        print(n)
