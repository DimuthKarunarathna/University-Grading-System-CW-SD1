## I declare that my work contains no examples of misconduct, such as plagiarism, or
##collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1898950
# Date:17/4/2022



def student_version_validation():
    
    print("------------(University Student Version Validation)---------------")

    
    #Creating Variable
    credit_pass=0
    credit_defer=0
    credit_fail=0
    total=0

    list1=[]#Empty list to add the user input
    #List for Range
    listed_credits=[0,20,40,60,80,100,120]

    while True:
        try:#Checking wheather userinput is integer
            credit_pass=int(input("\nPlease enter your credits at pass:\t"))
                                              #checking wheather user is within the Range
            if credit_pass in listed_credits:
                
                credit_defer=int(input("\nPlease enter your credits at defer:\t"))
                
                if credit_defer in listed_credits:
                    
                    credit_fail=int(input("\nPlease enter your credits at fail:\t"))
                    
                    if credit_fail in listed_credits:
                        
                        total = credit_pass+credit_defer + credit_fail
                        
                        if total==120:
                            break
                        #End of the Loop
                        
                        else:
                            print("\nTotal incorrect")
                            
                    else:
                        print("\nOut of range")
                        
                else:
                    print("\nOut of range")
                    
            else:
                print("\nOut of range")
                
        except:
            print("\nInteger required")


    #Append user input
    list1.append(credit_pass)
    list1.append(credit_defer)
    list1.append(credit_fail)


   #Reading user input and getting the result
    for x in list1:
        if list1[0]==120:
            print("\nProgress")
            break 
        elif list1[0]==100:
            print("\nProgress (module trailer)")
            break
        elif list1[2]>=80:
            print("\nExclude")
            break
        
        else:
            print("\nDo not progress – module retriever")
            break

student_version_validation()        
        
        
        

        
            
