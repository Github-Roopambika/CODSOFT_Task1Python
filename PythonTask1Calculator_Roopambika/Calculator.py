# Program to create a calculator by Roopambika Mohanty
def operation(): 
  a=int(input("Enter first number a=")) 
  b=int(input("Enter second number b="))
  selection=int(input("Choose operation(1/2/3/4) 1.Add 2.Subtract 3.Multiply 4.Divide(b!=0) ")) 
  match selection:
      case 1:
         print("Sum is" , a+b)
      case 2:
         print("Difference is" , a-b)
      case 3:
         print("Product is" , a*b)
      case 4:
        print("Quotient is" , a/b)
      case _:
         print("Invalid selection")
                  
while True:
   operation()
   
   response=input("Do you want to perform next operation? (yes/no)")
   if response=="no":
       print("Program ended successfully")
       break
   elif  response=="yes":
      continue
   else:
      raise ValueError("Invalid response")