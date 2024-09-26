def calculate_bmi(weight, height):

  bmi = weight / (height ** 2)
  return bmi

def interpret_bmi(bmi):

  if bmi < 18.5:
    return "Underweight"
  elif 18.5 <= bmi < 25:
    return "Normal"
  elif 25 <= bmi < 30:
    return "Overweight"
  else:
    return "Obese"

weight = float(input("Enter your weight in kilograms : "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

bmi_interpretation = interpret_bmi(bmi)

print("Your BMI is:", bmi)
print("BMI Interpretation:", bmi_interpretation)
