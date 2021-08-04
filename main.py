# a = bq + r

a = int(input('[+] Value of a: '))
b = int(input("[+] Value of b: "))
q = int(a/b)
r = a - b*q
print(a , "=" , b , "X" , q , "+" , r)
while r != 0:
    a = b
    b = r
    q = int(a/b)
    r = a - b*q
    print(a , "=" , b , "X" , q , "+" , r )
print("[+] HCF: " , b)
