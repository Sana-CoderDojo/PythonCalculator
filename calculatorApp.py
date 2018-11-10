num1 = input("Please enter the first number ")
num2 = input("Please enter the second number ")
print("What would you like to do with "+str(num1)+" and "+str(num2)+" ?")
action = raw_input("(Hint: Type 'multiply', 'add', 'divide' or 'subtract'!) ")

if(action=="add"):
    print("The sum of "+str(num1)+" and "+str(num2)+" is: "+str(num1+num2))
elif(action == "subtract"):
    print("The difference of "+str(num1)+" and "+str(num2)+" is: "+str(num1-num2))
elif(action == "multiply"):
    print(str(num1)+" multiplied by "+str(num2)+" is: "+str(num1*num2))
elif(action == "divide"):
    print(str(num1)+" divided by "+str(num2)+" is: "+str(num1/num2))
else:
    action = input("Error: Calculator failed to understand the action. \n Try typing 'add','subtract','multiply' or 'divide' ")