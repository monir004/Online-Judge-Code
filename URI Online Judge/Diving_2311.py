def min_max(arr):
    min_= max_ = arr[0]
    for i in arr[1:]:
        if i>max_: max_ = i
        if i<min_: min_ = i
    return min_,max_

def main():
    #print() prints a new line
    test_case = int(input())
    diver_names = []
    diver_scores = []
   
    for i in range(test_case):

        name = input()
        diver_names.append(name)

        diff = float(input())
        
        arr_scores = list(map(float, input().split()))
       
   
        mn, mx = min_max(arr_scores)

        sum=0.00
        for i in range(len(arr_scores)):
            if(arr_scores[i]!=mx and arr_scores[i]!=mn):
                sum+=arr_scores[i]

        sum=sum*diff
        diver_scores.append(sum)
    for i in range(test_case):
        print(diver_names[i],"%.2f" %diver_scores[i])

if __name__=="__main__":
    main()
