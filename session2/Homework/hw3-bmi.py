wei = float(input("wei (kg) = "))
hei = float(input("hei (cm) = "))
heim = hei / 100
bmi = wei / (heim ** 2)
print(bmi)

if bmi < 16:
    print("Severely underweight")

elif bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print("Normal")

elif bmi < 30:
    print("Overweight")

else:
    print("Obese")
