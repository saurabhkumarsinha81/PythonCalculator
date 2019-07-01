print("Welcome to the PYTHON CALCULATOR.")
try:
  num1=int(input('Enter the first number: '))
  num2=int(input('Enter the second number: '))
except:
    print("Please enter a numerical value!!")
else:
    
    x=5
    while(x!='0'):
        print("----Operations----: ")
        print("1- Addition")
        print("2- Subtraction")
        print("3- Multiplication")
        print("4- Division")
        print('0- EXIT')

        try:
            x=int(input("Choose the Operation: "))
        except:
            print('Error!!! Please Enter a numerical value')
            print()
            print()
        else:

            if(x==0):
                break
            elif(x==1):
                print("Addition: ",num1+num2)
                print()
                print()
            elif(x==2):
                print("Subtraction: ",num1-num2)
                print()
                print()    
            elif(x==3):
                print("Multiplication: ",num1*num2)
                print()
                print()
            elif(x==4):
                try:
                    div=num1/num2
                    print("Division: ",div)
                    print()
                    print()
                except:
                    print("Error!! Cannot Divide by zero")
                    print()
                    print()
            else:
                print("Incorrect Choice!!")
                print()
                print()
