number=int(input("Enter decimal number:"))
x=number
power_2_gen=0
power_2_list=[]
base_2=[]

for i in range(1,number):
    result = 2**power_2_gen
    power_2_gen+=1
    if result >= number:
        break
    else:
       power_2_list.append(result)
power_2_list.reverse()

for j in power_2_list:
    if j <= number:
        base_2.append(1)
        number -= j
    else:
        base_2.append(0)
answer="".join(str(p) for p in base_2)
print(f"{x} in base 2 = {answer}")