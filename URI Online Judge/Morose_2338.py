def letter_return(s):
   morse_dict = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e":  ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
        }
   for x in morse_dict:
       if(morse_dict[x]==s):
           return x



def main():
    test_case=int(input())
    for j in range(test_case):
        codes = input()
        length = len(codes)
        string=""
        temp = ""
        result = ""
        i=0
        while i<length:
            if(codes[i]=="="):
                temp+=codes[i]
            else:
                if(temp=="="):
                    string+="."
                    temp=""
                elif(temp=="==="):
                    string+="-"
                    temp=""
                if(codes[i+1]=="."):
                    flag=True
                    count=1
                    while(flag==True):
                        if(codes[i+1]=="."):
                            count+=1
                            i+=1
                        elif(codes[i+1]!="."):
                            flag=False
                    if(count==3):
                        result+=letter_return(string)
                        string=""
                    elif(count==7):
                        result+=letter_return(string)
                        result+=" "
                        string=""
            i+=1
        else:
            if(temp=="="):
                string+="."
                temp=""
            elif(temp=="==="):
                string+="-"
                temp=""
            result+=letter_return(string)
            print(result)



if __name__=="__main__":
    main()