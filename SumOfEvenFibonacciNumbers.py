# https://projecteuler.net/problem=2
fibonacci = 0
firstNumber = 0
secondNumber = 1
total = 0
while fibonacci < 4000000 :
  fibonacci = firstNumber + secondNumber
  firstNumber = secondNumber
  secondNumber = fibonacci
  if fibonacci % 2 == 0 :
    total = total + fibonacci
print total
