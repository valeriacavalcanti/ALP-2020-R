def misterio1():
    return misterio2() + 1

def misterio2():
    return misterio3() + 2

def misterio3():
    return misterio4() + 3

def misterio4():
    return 4

# Programa Principal

print(misterio1())
