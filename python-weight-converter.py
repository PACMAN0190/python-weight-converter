weight = float(input("enter the weight:"))
unit = input("kilograms or pounds? (k or l): ")
if unit == "k":
   weight =  weight * 2.205
   unit = "lbs."
elif unit == "l":
   weight = weight / 2.205
   unit = "kgs."
else:
   print(f"{unit} was not valid")
print(f"your weight is:{round(weight, 1)} {unit}")

weight = float(input("enter the weight:"))
width = float(input("enter the width:"))
height = float(input("enter the height:"))
area = weight * width * height
print(f"the area is {area}")
