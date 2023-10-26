# calculator program
from art import logo

# adding two numbers
def add(n1,n2):
  return n1+n2
# substracting two numbers
def sub(n1,n2):
  return n1-n2
# multiply two numbers
def mult(n1,n2):
  return n1*n2
# deviding two numbers
def div(n1,n2):
  return n1/n2
# -------------------------------------------------------------------
operation={
    "+":add,
    "-":sub,
    "*":mult,
    "/":div,
           }
def calculator():
 print(logo)
 num1=float(input("what is the first number:"))
 for symbol in operation:
   print(symbol)
 should_continue=True
 while should_continue:
  chosen_operation=input("pick an operation :")
  num2=float(input("what is the next number:"))
  calculation=operation[chosen_operation]
  answer=calculation(num1,num2)
  print(f"{num1}{chosen_operation}{num2}={answer}")
  ask_user_continue=input(f"Type 'y' to continue calculating with {answer},or type'no' to start a new calculating:")
  if ask_user_continue=="y":
    num1=answer
  elif ask_user_continue=="no":
    should_continue=False
    calculator() 
calculator()