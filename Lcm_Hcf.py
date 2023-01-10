import pyfiglet as figlet
import math as numpy

print("Devloped and created by Satya\n")

print(figlet.figlet_format("LCM AND HCF\n"))

print("Calculator\n")

print("Instruction: \n Please turn on your CAPS LOCK or type LCM or HCF in capital and typing yes or no please enter y or n. Thankyou!\n")

operation = str(input("Do you want to calculate LCM or HCF, type LCM for lcm and HCF for hcf: \n"))

num1 = int(input("Enter your first number: \n"))
num2 = int(input("Enter your second number: \n"))

if operation == 'HCF':
    var = str(input("Do you want to add third no. to calculate y/n: "))
    if var == 'y':
        num3 = int(input("Enter your third number: "))
        print("Your number: \n")
        print(numpy.gcd(num1,num2,num3))
    else:
        print("Your number \n")
        print(numpy.gcd(num1,num2))

          
elif operation == 'LCM':
    var1 = str(input("Do you wnat to add third number y/n: "))
    if var1 == 'y':
        num3 = str(input("Enter your third number: "))
        print("Your number: \n")
        print(numpy.lcm(num1,num2,num3))
    else:
        print("Your number \n")
        print(numpy.lcm(num1,num2))


print("Thankyou for using our calculator>./-")


