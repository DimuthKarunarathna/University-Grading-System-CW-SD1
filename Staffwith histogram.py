## I declare that my work contains no examples of misconduct, such as plagiarism, or
##collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1898950
# Date:17/4/2022



def staff_version_with_histogram():

        print("---------------Staff Version with Horizontal Histogram---------------")



        #creating Variable
        Progress= 0
        Trailing= 0
        Retriever= 0
        Excluded= 0

            
                

        def process_credit(x):
            name = input(x)
            try:
                name = int(name)
                if name in range(0, 121, 20):
                    return name
                else:
                    print("\nRange Error...")
                    print("\nTry again...")
                    return  process_credit(x)
            except ValueError:
                print(" Please enter integer value of credit...")
                print(" Try again...")
                return Staff_Version_with_Horizontal_Histogram(x)

        while True:
            Pass=process_credit("\nEnter your number of pass credit:\t")
            Defer = process_credit("\nEnter your number of defer credit:\t")
            Fail =process_credit("\nEnter your number of fail credit:\t")

            total_credit = Pass + Defer + Fail
            if total_credit != 120:
                print("\nYour total credit is incorrect")
                print("\nTry again")

            elif Pass == 120 and Defer == 0 and Fail == 0:
                print("Progress")
                Progress = Progress + 1

            elif Pass==100 and (Defer in range(0,21,20)) and (Fail in range(0,21,20)):
                print("Progress – module trailer")
                Trailing = Trailing + 1

            elif (Pass in range(0,81,20)) and (Defer in range(0,121,20)) and (Fail in range(0,61,20)):
                print("Do not Progress – module retriever")
                Retriever = Retriever + 1

            elif (Pass in range(0,41,20)) and (Defer in range(0,41,20)) and (Fail in range(80,121,20)):
                print("Exclude")
                Excluded = Excluded + 1

            else:
                print("Something went wrong...")

            print()
            End = str.lower(input("Press 'q' to quit the program or Press any button to continue: "))
            if End == "q":
                break

            else:
                print()
                print('Enter your credits')

        print("\tProgress\t", Progress,":", "*"*Progress)
        print("\tTrailing\t", Trailing,":", "*"*Trailing)
        print("\tRetriever\t", Retriever,":", "*"*Retriever)
        print("\tExcluded\t", Excluded,":", "*"*Excluded)
        total = Progress + Trailing + Retriever + Excluded
        print("\t",total,"outcomes in total")
staff_version_with_histogram()



