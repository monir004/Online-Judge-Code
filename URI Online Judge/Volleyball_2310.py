
def main():
    test_case = int(input())
    arr = []
    for _ in range(test_case):
        name = input()
        a, b, c = input().split()
        d, e, f = input().split()
        arr.append(int(a))
        arr.append(int(b))
        arr.append(int(c))
        arr.append(int(d))
        arr.append(int(e))
        arr.append(int(f))
    j=3
    jump=0
    arr2 = []
    sum1=0
    sum2=0
   
    for i in range(3):
        for k in range(test_case):
            sum1 += arr[i+jump]
            sum2 += arr[j+jump]
            jump+=6

        arr2.append(sum1)
        arr2.append(sum2)
        sum1=0
        sum2=0
        j+=1
        jump=0
    
    print("Pontos de Saque: %.2f" %(arr2[1]/arr2[0]*100),"%.")
    print("Pontos de Bloqueio: %.2f" %(arr2[3]/arr2[2]*100),"%.")
    print("Pontos de Ataque: %.2f" %(arr2[5]/arr2[4]*100),"%.")


if __name__ == "__main__":
    main()