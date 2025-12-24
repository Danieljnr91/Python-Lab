def multiplication_table(num,ranges):
    multiplier=0
    emp_list=[]
    for i in range(1,ranges+1):
        answer= i * num
        multiplier+=1
        print(f"{num} x {multiplier} = {answer}")
        emp_list.append(answer)
    print(emp_list)


number=int(input("Enter number you wish to generate the multiplicatio table for\n:"))
end = int(input("Enter number where u want to mulitply up to\n:"))
multiplication_table(number,end)