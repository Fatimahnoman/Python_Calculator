#                            "CLASS # 7"   
#                       "CALCULATOR ASSIGNMENT"

# Creating Functions 

def addition(a,b):
    return a + b 
def subtraction(a , b):
    return a - b
def multiply(a , b):
    return a * b
def divide(a , b):
    return a / b

# Now im giving hints which operators you can simply use in this calculator

operation_dict ={
    "+" : addition,
    "-" : subtraction,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    value1 = int(input("Enter First Number: "))
    for symbol in operation_dict:
        print(symbol)

    continue_flag = True
    while continue_flag:
# Now im giving chance to user to pick one of an operator!    
        op_symbol = input("Pick an Operation: ")  
        
# Now im giving another chance to user to give another num with which he/she wants to do calculation
        value2 = int(input("Enter Second Num: "))

        calculator_func = operation_dict[op_symbol] #add

        output = calculator_func(value1,value2)

        print(f"{value1} {op_symbol} {value2} = {output}")

        should_continue = input(f"Enter 'y' to Continue Calculation with {output} or 'n' to start a new Calculation or 'x' to exit: ")
        if should_continue == 'y':
            value1 = output
        
        elif should_continue == 'n':
            continue_flag= False
            calculator()
        
        else:
            continue_flag = False
            print("Calculator Closed!")
calculator()















