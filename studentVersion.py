## I declare that my work contains no examples of misconduct, such as plagiarism, or
##collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1898950
# Date:17/4/2022

#Creating the variable
credit_pass=0
credit_defer=0
credit_fail=0

print("\n--------(University Student Version)------------")


def student_version():

    #Input the user Data
    credit_pass=int(input("\nPlease enter your credits at pass:\t"))
    credit_defer=int(input("\nPlease enter your credits at defer:\t"))
    credit_fail=int(input("\nPlease enter your credits at fail:\t"))

    #Getting the output
    if credit_pass == 120:
        print("\nProgress")

    elif credit_pass== 100:
        print("\nProgress (module trailer)")

    elif credit_fail>= 80:
        print("\nExclude")
           
    else:
        print("\nDo not progress – module retriever")
student_version()







        
