from timeit import default_timer as timer
from sympy.ntheory import factorint

def find_max_div_1(n):
    i = 2
    while i * i <= n:
        if not n % i == 0:
            i += 1
        else:
            while n % i == 0:
                n = n // i
    rez = n
    if n == 1:
        rez = i
    return rez

def find_max_div_2(n):
    z = factorint(n)
    return max(z)

def find_max_div(n):
    if n < 1e12:
        return find_max_div_1(n)
    else:
        return find_max_div_2(n)

def main(n = int(input("Input number:"))):
    print("n =", n)
    start_time = timer()
    rez = find_max_div(n)
    end_time = timer()
    print("time = ", end_time - start_time, 's')
    print("Max prime diviser =", rez)

if __name__ == "__main__":
    main()