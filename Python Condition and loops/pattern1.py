# 4. Write a Python program to construct the following pattern, 
# using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
n=5
for i in range(n+1):
    for j in range(i):
        print('*', end=' ')
    print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()