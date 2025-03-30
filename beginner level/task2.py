#1. You have a list of superheroes representing the Justice
#League. 
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"] 

#1. Calculate the number of members in the Justice League.
print("1.number of members:")
print(len(justice_league))
print(justice_league)

#2. Batman recruited Batgirl and Nightwing as new members.
#Add them to your list.
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("2.After adding Batgirl and Nightwing")
print(justice_league)

#3. Wonder Woman is now the leader of the Justice League.
#Move her to the beginning of the list.

temp=justice_league[0]
justice_league[0]=justice_league[2]
justice_league[2]=temp
print("3.After moving wonder woman to the beginning of the list")
print(justice_league)


#4. Aquaman and Flash are having conflicts, and you need to
#separate them. Choose either "Green Lantern" or "Superman"
#and move them in between Aquaman and Flash.
temp=justice_league[2]
justice_league[2]=justice_league[3]
justice_league[3]=temp
print("4.After separating aquaman and flash")
print(justice_league)


#5. The Justice League faced a crisis, and Superman decided to
#assemble a new team. Replace the existing list with the following
#new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".
justice_league=["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("5.After assembling a new team")
print(justice_league)


#6. Sort the Justice League alphabetically. The hero at the 0th
#index will become the new leader
justice_league.sort()
print("6.After sorting the list alphabetically")
print(justice_league)


new_leader=justice_league[0]
print("The new leader is",new_leader)