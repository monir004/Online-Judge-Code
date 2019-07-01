

def main():
    test_case=True
    while test_case==True:
        num = int(input())
        if num<0:
            test_case=False
        else:
            if num==0:
                print("0")
            else:
                print(num-1)



if __name__=="__main__":
    main()
