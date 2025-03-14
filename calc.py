num1 = int(input("Choose first number"))
num2 = int(input("choose second number"))
sign = input("sign")
if sign == "+":
 result = num1 + num2
 print(result)
elif sign == "-":
 result = num1 - num2
 print(result)
elif sign == "*":
  result = num1 * num2
  print(result)
elif sign == "/":
 result = num1 / num2
 print(result)
else:
 print("invalid")
