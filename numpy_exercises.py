import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print(a[a<0])
print(a[a<0])
L1 = (a[a>0])
l2 = (a[a % 2 == 0])
print(l2)
b = a[a>0]
print(len(b[b % 2 == 0]))
#%%
c1 = a + 3
print(len(c[c>0]))
d1 = a ** 2
print(np.std(d1), np.mean(d1))
#%%
a_centered = np.mean(a) - a
print(a_centered)
a_zscore = a_centered / np.std(a)
print(a_zscore)
#%% More Numpy Exercises
import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = (a.sum())
print(sum_of_a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_a = (a.min())
print(min_a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_a = max(a)
print(max_a)
#%%
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = np.mean(a)
print(mean_of_a)
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = np.prod(a)
print(product_of_a)
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = a ** 2
print(squares_of_a)
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = a[a % 2 != 0]
print(odds_in_a)
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a[a % 2 == 0]
print(evens_in_a)
#%%
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b = (b.sum())
print(sum_of_b)
# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

print(b.min())
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

print(b.max())
# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
#%%
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
print(np.prod(b))
# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

print(np.cumprod(b))
# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

print(b[b % 2 != 0])
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
print(b[b % 2 == 0])
# Exercise 9 - print out the shape of the array b.
print(b)
# Exercise 10 - transpose the array b.
print(np.transpose(b))
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print(b.reshape(1,6))
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print(b.reshape(6,1))
#%%
## Setup 3
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
print(c.sum(), c.min(), c.max())
c_prod = c.cumprod()
c_prod.reshape(3,3)
print(c_prod.reshape(3,3))
# Exercise 2 - Determine the standard deviation of c.
print(c.std())
# Exercise 3 - Determine the variance of c.
print(c.var())
# Exercise 4 - Print out the shape of the array c
print(np.shape(c))
# Exercise 5 - Transpose c and print out transposed result.
print(np.transpose(c))
# Exercise 6 - Get the dot product of the array c with c. 
print(np.dot(c, c))
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
c_transposed = np.transpose(c)
c_x_ct = c * c_transposed
print(np.sum(c_x_ct))
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print(np.prod(c_x_ct))
#%%
## Setup 4
d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

# Exercise 1 - Find the sine of all the numbers in d
print(np.sin(d))
# Exercise 2 - Find the cosine of all the numbers in d
print(np.cos(d))
# Exercise 3 - Find the tangent of all the numbers in d
print(np.tan(d))
# Exercise 4 - Find all the negative numbers in d
print(d[d % 2 != 0])
# Exercise 5 - Find all the positive numbers in d
print(d[d % 2 == 0])
# Exercise 6 - Return an array of only the unique numbers in d.
print(np.unique(d))
# Exercise 7 - Determine how many unique numbers there are in d.
print(len(np.unique(d)))
# Exercise 8 - Print out the shape of d.
print(np.shape(d))
# Exercise 9 - Transpose and then print out the shape of d.
d_transposed = np.transpose(d)
print(np.shape(d_transposed))
# Exercise 10 - Reshape d into an array of 9 x 2
print(d.reshape(9,2))