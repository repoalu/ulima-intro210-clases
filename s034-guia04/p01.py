def mayor(a, b):
    if(a > b):
        return a
    else:
        return b

def mayor3(a, b, c):
    mayor_ab = mayor(a, b)
    res = mayor(mayor_ab, c)
    return res

def main():
    n1 = 127
    n2 = 156
    n3 = 77
    res = mayor3(n1, n2, n3)
    print("El mayor es: ", res)

if __name__ == "__main__":
    main()