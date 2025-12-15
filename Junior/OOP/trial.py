# x=3
# y=4
# z=x
# x=y
# y=z
# print(x)
# print(y)

# y = [3,4,5,7,5,43,2,4,5,7,8,92,3,3,4,5,67,8,8,6,4,3,2,90]
# for i in y:
#   k=y.index(i)
#   for k in range(len(y)-1):
#    if y[k] > y[k+1]:
#     swap = y[k]
#     y[k]=y[k+1]
#     y[k+1]=swap
#     print(y)


# numbers = [5, 3, 8, 1]
# for i,x in enumerate(numbers , start=1):
#   print(i,x)

# students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
# for i , j in students:
#   print(i,j)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for i , j in zip(names,scores):
  print(i,j)