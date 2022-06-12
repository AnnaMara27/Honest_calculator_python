msg = ["Enter an equation", "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
       "Yeah... division by zero. Smart move...", "Do you want to store the result? (y / n):",
       "Do you want to continue calculations? (y / n):", " ... lazy", " ... very lazy", " ... very, very lazy",
       "You are", "Are you sure? It is only one digit! (y / n)",
       "Don't be silly! It's just one number! Add to the memory? (y / n)",
       "Last chance! Do you really want to embarrass yourself? (y / n)"]

def is_one_digit(v):
    if float(v) > -10 and float(v) < 10 and float(v).is_integer() == True:
        return True
    else:
        return False

def check(v1, v2, v3):
    msg_ = ""    
    if is_one_digit(v1) == True and is_one_digit(v2) == True:
        msg_ = msg_ + msg[6]
    if (float(v1) == 1 or float(v2) == 1) and v3 == "*":
        msg_ = msg_ + msg[7]
    if (float(v1) == 0 or float(v2) == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg_ = msg_ + msg[8]
    if msg_ != "":
        msg_ = msg[9] + msg_
        print(msg_)
    return

def is_digit(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
       
def get_result(oper):
    if oper == "+":
        return float(x) + float(y)
    elif oper == "-":
        return float(x) - float(y)
    elif oper == "*":
        return float(x) * float(y)
    elif oper == "/":
        if int(y) != 0:
            return float(x) / float(y)
        else:
            print(msg[3])#division by zero
        
def store_result():
    while True:
        choice = input(msg[4] + "\n") #store the result? (y / n):
        if choice == "y":
            False
            return True
        elif choice == "n":
            False
            return False
        else:
            continue
        return
        
def store_in_memory():
    msg_index = 10
    while True:
        answer = input(msg[msg_index])
        if answer == "y":
            if msg_index < 12:
                msg_index += 1
                continue
            else:
                return True
        elif answer == "n":
            return
        else:
            continue
    
def continue_calculations():
    while True:
        answer = input(msg[5] + "\n")#continue calculations? (y / n):
        if answer == "y":
            False
            return True
        elif answer == "n":
            False
            return False
        else:
            continue
        
memory = 0
while True:
    print(msg[0]) #enter an equation
    equation = input()
    x = equation[0:equation.index(" ")]
    y = equation[equation.rfind(" ") + 1:]
    oper = equation[equation.index(" ") + 1:equation.rfind(" ")]

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    if is_digit(x) == False or is_digit(y) ==  False:
        print(msg[1]) #o you even know what numbers are?
    else:        
        if oper != "+" and oper != "-" and oper != "*" and oper != "/":
            print(msg[2]) #an interesting math operation
        else:            
            check(x, y, oper)
            if get_result(oper) == None:
                continue
            else:
                result = get_result(oper)
                print(result)
            
                if store_result() == True:
                    if is_one_digit(result) == True:
                        if store_in_memory() == True:
                            memory = result
                    else:
                        memory = result

                if continue_calculations() == True:
                    continue
                else:
                    break
                    