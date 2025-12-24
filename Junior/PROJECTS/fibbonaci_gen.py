limit = int(input("Where do you want to generate up to?:"))
fib_list=[0,1]
for i in range(1,limit+1):
    fibbonaci = fib_list[i] + fib_list[i-1]
    fib_list.append(fibbonaci)
    print(" ".join(str(i) for i in fib_list))


