BMI=int(input())
if BMI<18:
    print("Underweight")
elif 18<=BMI<=24:
    print("Normal weight")
elif 25<=BMI<=29:
    print("Overweight")
else:
    print("Obese")
