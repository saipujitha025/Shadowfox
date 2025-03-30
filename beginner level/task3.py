#program to determine the BMI Category based on user input
Height=float(input("Enter height in meters:"))
Weight=float(input("Enter weight in kilograms:"))

bmi=Weight/(Height**2)


if bmi>=30:
    print ("bmi category is Obesity")
elif 25<=bmi<29:
    print ("bmi category is Over weight")
elif 18.5<=bmi<25:
    print("bmi category is normal")
else:
    print("under weight")



#program to determine which country a city belongs to
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city=input("Enter a city name:")
if city in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
    print(city +" "+"belongs to australia")
elif city in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
    print(city + " " +"belongs to UAE")
elif city in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
    print(city + " " + "belongs to India")
else:
    print ("city is not found")


#program to check if two cities belong to the same country
first_city=input("Enter the first city:")
second_city=input("Enter the second city:")
if first_city in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
    first_country="australia"
elif first_city in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
    first_country="UAE"
elif first_city in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
    first_country="India"
else:
    first_country="none"
if second_city in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
    second_country="australia"
elif second_city in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
    second_country="UAE"
elif second_city in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
    second_country="India"
else:
    second_country="none"

if first_country==second_country:
    print("Both cities are in"+ " " + first_country)
else:
    print("They don't belong to the same country")



