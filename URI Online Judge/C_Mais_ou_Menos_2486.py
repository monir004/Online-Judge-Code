def vitamin_c_of(food_name):
    vitamin_c_table = {
        "suco de laranja":120,
        "morango fresco":85,
        "mamao":85,
        "goiaba vermelha":70,
        "manga":56,
        "laranja":50,
        "brocolis":34
        }

    for x in vitamin_c_table:
        if(x==food_name):
            return vitamin_c_table[x]



def main():

    bool_breaking_condition=True
    while(bool_breaking_condition==True):
        test_case = int(input())
        if(test_case>0):
            total_vitamin_c_consumed=0
            for i in range(test_case):
                amount,food_name=input().split(" ",1)
                total_vitamin_c_consumed+=int(amount)*vitamin_c_of(food_name)
            else:
                if(total_vitamin_c_consumed>=110 and total_vitamin_c_consumed<=130):
                    print(total_vitamin_c_consumed,"mg")
                elif(total_vitamin_c_consumed<110):
                    print("Mais",110-total_vitamin_c_consumed,"mg")
                elif(total_vitamin_c_consumed>130):
                    print("Menos",total_vitamin_c_consumed-130,"mg")
        else:
            bool_breaking_condition=False

if __name__=="__main__":
    main()
