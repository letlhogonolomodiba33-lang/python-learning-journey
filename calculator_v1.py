

again="yes"

while again=="yes":
  Num1=int(input("Enter first number"))
  Num2=int(input("Enter second number"))

  print("1) is for Addition")
  print("3) is for multiplication")
  print("4) is for Division")

  Choice=input("Enter choice ")




  def add (a,b):
    print("addition is :" , a+b)
    ...

  def sub (a,b):
     print("subtraction is :", a-b )
     ...

  def multi (a,b):
     print("multiplication is :" , a*b)
     ...
  def div (a,b):
     print(" division is :" , a/b)
     ...



  if Choice=="1":
      add(Num1, Num2)
  elif Choice=="2":
     sub(Num1,Num2)
  elif Choice=="3":
     multi(Num1,Num2)
  elif Choice=="4":
     div(Num1,Num2)
  else:
     print("invalid input")


  again=input("do you want to calculate again (yes/no)")
  if again=="no":
     print("Thanks for using our program")






