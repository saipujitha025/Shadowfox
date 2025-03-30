print("1.program to stimulate rolling sixsided dice")
import random
rolls=20
count_6=0
count_1=0
consecutive_6=0
previous_roll=0
for _ in range(rolls):
    roll=random.randint(1,6)
    print("Dice Rolled:" ,roll)
    if roll==6:
        count_6+=1
        if previous_roll==6:
            consecutive_6 +=1
        
    elif roll==1:
        count_1 +=1

    previous_roll=roll

print("\n Statistics")
print("Number of times 6 is rolled:",count_6)
print("Number of times 1 is rolled:",count_1)
print("Number of times two consecutive 6 are rolled:", consecutive_6)


#2.program on jumping jacks
number_of_jacks=100
set_of_jacks=10

for completed in range(set_of_jacks,number_of_jacks+1,set_of_jacks):
    print("perform"," ",set_of_jacks," ","jumping jacks")

    if completed>=number_of_jacks:
        print("Congratulations! You completed the workout")
        break
    response=input("Are you tired?(yes/no):")
    if response in ["yes","y"]:
        skip=input("Do you want to skip the remaining sets? (yes/no):")
        if skip in ["yes","y"]:
            print("You have completed a total of"," ", completed ," ","jumping jacks.")
            break
    
    remaining=number_of_jacks-completed
    print(remaining," ","jumping jacks remaining.")
