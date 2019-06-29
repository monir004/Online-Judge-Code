def main():
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    #print(type(a))
    if a==b or a==c or b==c or a+b==c or a+c==b or b+c==a:
        print("S")
    else:
        print("N")
#python print() function by default ends with newline. 
#Python has a predefined format if you use print(a_variable)
# then it will go to next line automatically.
if __name__ == "__main__":
    main()
