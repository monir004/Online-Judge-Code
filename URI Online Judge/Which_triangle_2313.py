def pythagorean_triangle_check(a,b,c):
    a_s=a*a
    b_s=b*b
    c_s=c*c
    if(a_s+b_s==c_s or b_s+c_s==a_s or c_s+b_s==a_s):
        return True
    else:
        return False



def main():
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if(a+b<=c or b+c<=a or c+a<=b):
        print("Invalido")
    else:
        if(a==b==c):
            print("Valido-Equilatero")
            print("Retangulo: N")
        elif (a==b or b==c or c==a):
            print("Valido-Isoceles")
            print("Retangulo: N")
        else:
            print("Valido-Escaleno")
            if (pythagorean_triangle_check(a,b,c)):
                print("Retangulo: S")
            else:
                print("Retangulo: N")

if __name__=="__main__":
    main()

