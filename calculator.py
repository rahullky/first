num1=int(input("Enter the Value no..1.."))
num2=int(input("Enter the Value no..2.."))
oprt=input("Enter the oprt ....")

if oprt=="+":
    print(num1+num2)
elif oprt == "-":
    print( num1 - num2 )
elif oprt == "*":
    print( num1 * num2 )
elif oprt == "/":
    print( num1 / num2 )
elif oprt == "**":
    print( num1 ** num2 )
elif  oprt == "//":
    print( num1 // num2 )
else:
    print("Try something oprt Sign")