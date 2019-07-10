def main():
    test_case=int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count=0
    i=1
    while i<test_case:
        if arr[i]==arr[i-1]:
            count+=1
            i+=2
        else:
            i+=1
    print(count)
if __name__=="__main__":
    main()
