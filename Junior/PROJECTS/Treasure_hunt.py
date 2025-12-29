import random

row1=['_','_','_']
row2=['_','_','_']
row3=['_','_','_']
matrix_nested=[row1,row2,row3]



def game_output(coord_list,comp_list,matrix_nest):
    row_number=coord_list[0]
    column_number=coord_list[1]
    if coord_list != comp_list:
        print("Treasure Not Found, Try Again")
        matrix_nest[row_number][column_number]="X"
      
    else:
        print("Ayyee ye Skellywag,You found us some treasure!!")
        matrix_nest[row_number][column_number]="💎"
    for i in matrix_nest:
        print(i)
        
        
coordinates=[0,1,2]
computer_choice=random.choices(coordinates,k=2)
print(computer_choice)

chances=0
while chances < 6:
    user_coord = input("Enter Your coordinates separated by comma: ").split(',')
    user_coord_list = [int(i) for i in user_coord]

    game_output(user_coord_list, computer_choice, matrix_nested)
    chances += 1

    if any("💎" in j for j in matrix_nested):
        break

if not any("💎" in j for j in matrix_nested):
    print(f"Ayee, better luck next time captain")
    print(f"The treasure was at coordinate {computer_choice}")
    