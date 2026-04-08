def add(a: float, b: float) -> float:
  return a + b

def subtract(a: float, b: float) -> float:
  return a - b  

def multiply(a: float, b: float) -> float:
  return a * b

def divide(a: float, b: float) -> float:
  if b == 0:
    raise ValueError("Cannot divide by zero")
  return a / b  

def power(a: float, b: float) -> float:
  return a ** b

def calculate(a: float, b: float, operator: str) -> float:
  if operator == "+":
    return add(a, b)
  elif operator == "-":
    return subtract(a, b)
  elif operator == "*":
    return multiply(a, b)
  elif operator == "/":
    return divide(a, b)
  elif operator == "**":
    return power(a, b)
  else:
    raise ValueError("Invalid operator")
  
# Example usage:
result = calculate(10, 5, "+")

def greet():
  name = input("Enter your name: ")
  print("hello " + name)

greet()

