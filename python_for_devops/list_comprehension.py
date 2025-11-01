# to easily loop through list elements without writing mulitple line of for loops


x =[i for i in range(0, 10)]

print(x)

# for printing a permutation of number from range of 5 not adding up to 3

y = [[i,j] for i in range(5) for j in range(5) if i + j != 3]

print(y)