# https://projecteuler.net/problem=1
multiplesOf3 = range(0,1000,3)
multiplesOf5 = range(0,1000,5)
multiplesOf3And5List = multiplesOf3 + multiplesOf5
multiplesOf3And5Set = set(multiplesOf3And5List)
total = sum(multiplesOf3And5Set)
print total
