import pyfiglet as figlet
import math 

print(figlet.figlet_format("LCM and HCF"))
print("Calculator")

print("Created and devloped by D.Satya.")

print(figlet.figlet_format("LCM"))

no1 = int(input("Enter your first number: "))
no2 = int(input("Enter your second number: "))

print("\n")

yorno = str(input(" Do you want to add third number to calculate y/n: "))

if yorno == "y":
    no3 = int(input("Enter your third number: "))
    print("Your number: ")
    print(math.lcm(no1,no2,no3))

elif yorno == "n":
    print("Your number: ")
    print(math.lcm(no1,no2))

hcf = str(input("Do you want to use our HCF Program y/n: "))

if hcf == "y":
    hc1 = int(input("Input your first number to calculate: "))
    hc2 = int(input("Enter your second number to calculate: "))
    hcyn = input("Do you want to add third number to calculate y/n: ")

    print("Your number: ")
    print(math.gcd(hc1,hc2))

    if hcyn == "y":
        hc3 = int(input("Enter your third number: "))
        print(math.gcd(hc1,hc2,hc3))
    
    elif hcyn == "n":
        pass


elif hcf == "n":
    print("Thankyou for using our calculator")
    exit




    







