num1 = int(input("Enter the first number: ")) 
num2 = int(input("Enter the second number: "))
op = input ("Choose the operation (+, -, *, /): ")
if num2 == 0 and op == "/" :
    print("Cannot divide by zero.")
else : 
    match op : 
      case "+":
        result = num1 + num2 
        print(f"The result is {result}.")  
      case "/":
        result = num1 / num2 
        print(f"The result is {result}.") 
      case "-":
        result = num1 - num2 
        print(f"The result is {result}.")   
      case "*":
        result = num1 * num2 
        print(f"The result is {result}.")   
