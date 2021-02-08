a=float(input("Enter your height(cm):"))
b=float(input("Enter your weight(kg):"))

k=b/(a/100)**2

if k<=0:
    print("Please enter your real height and weight...")
elif k<=18.5:
    print("Your BMI: {} ***WEAK***".format(k))
elif k<=25:
    print("Your BMI: {} ***NORMAL***".format(k))
elif k<=30:
    print("Your BMI: {} ***OVERWEIGHT***".format(k))
