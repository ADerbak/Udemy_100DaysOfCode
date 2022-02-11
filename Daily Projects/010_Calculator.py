# Import Packages:
import art



# Define Calculator Functions

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  # Print Logo
  print(art.logo)
  num1 = float(input("What is the first number?: "))
  num2 = float(input("What is the second number?: "))
  print("Which operation would you like to do?")
  for i in operations:
    print(i)

  op = input("Please pick an operation from the list above: \n")

  function = operations[op]
  answer = function(num1,num2)
  print(f"{num1} {op} {num2} = {answer}")

  calculate = True

  while calculate:
    continue_calculate = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.:")
    if continue_calculate == 'y':
      op = input("Please pick an operation: ")
      next_number = float(input("What's the next number?: "))
      function = operations[op]
      prev_number = answer
      answer = function(answer,next_number)
      print(f"{prev_number} {op} {next_number} = {answer}")
    else:
      print("\n\n..Starting New Calculation...")
      calculate = False
      calculator() # Recursive call to start fresh!

calculator()