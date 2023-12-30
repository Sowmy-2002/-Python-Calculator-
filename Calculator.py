#Enter the input from the user

a = input("Enter choice (1/2/3/4/5): ")

#Enter 2 numbers......2 numbers can be integer instead of float

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

#Perform looping

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
#If the user chooses to exit (Option 5), the program prints an exit message and breaks out of the loop.

    if a == '5':
        print("Exit")
        break
    
#If given number not equal user input,then we have to enter valid choice

    if a not in ('1', '2', '3', '4'):
        print("Enter a valid number.")
        continue
    
#If given number equal 1 perform add:
    
    if a == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
        
#If given number equal 2 perform subtraction:
        
    elif a == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

#If given number equal 3 perform multiplication:
        
    elif a == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
        
#If the user chooses division, the program checks if the second number (num2) is not zero to avoid division by zero errors.
        
    elif a == '4':
        
       if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
       else:
            print("Cannot divide by zero")



    a1 = input("Do you want to exit the calculation?: ")
    
    if a1 == 'yes':
        print("Exit.Goodbye!")
        break
    
        
   
 
