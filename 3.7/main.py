#weight = float(input("What is your weight? "))
#unit = input("Kgs or Lbs? ")
#pound = 2.20462
#converted_weight = float(weight * pound)
#formatted_float = "{:.2f}".format(converted_weight)
#
#print(weight)
#print(unit)
#
#if unit == "Kgs":
#    print(f"Your weight is {weight} {unit}")
#elif unit == "Lbs":
#    print(f"Your weight is {formatted_float} {unit}.")
#else:
#    print("That is not a valid input. Please try again.")

weight = float(input("Please enter your weight for conversion: "))
unitForConversion = input("(K)Kgs and (L)Lbs? ")
pound = 2.20462

weightConverted = float(weight * pound)

if unitForConversion == "K":
    weightConvertedInt = int(weightConverted)
    print("Your weight is", weightConvertedInt, "in killograms. (Rounded to the nearest whole number)")
elif unitForConversion == "L":
    weightConvertedInt = int(weightConverted)
    print("Your weight is", weightConvertedInt, "in pounds. (Rounded to the nearest whole number)")
else:
    print("The numbers you have entered are invalid.")