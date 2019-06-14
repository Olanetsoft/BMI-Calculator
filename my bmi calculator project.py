#bmi calculator
print("YOU ARE WELCOME TO BMI CALCULATOR BUILT BY IDRIS")
print("")
print(" PLEASE KINDLY ENTER YOUR VALUE IN KG FOR WEIGHT AND IN METERS FOR HEIGHT ")
print("")
w=float(input("please enter the value for weight in KG = "))
print("")
h=float(input("please enter the value for height in METERS = "))
bmi=w/(h*h)
answer=round(bmi,1)
print("")
if (answer<18.5):
    print("UNDERWEIGHT")
elif ((answer>=18.5) and (answer<=25)):
    print("NORMAL")
elif ((answer>=25)and(answer<=30)):
    print("OVERWEIGHT")
elif (answer>30):
    print("obese")
else:
    print("RE-TRY")
