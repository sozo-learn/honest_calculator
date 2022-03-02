msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
checks = [msg_10, msg_11, msg_12]

ops = "+-*/"
memory = 0
result = 0

running = True


def is_one_digit(v):
    if -10 < v < 10 and v == int(v):
        return True
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while running:
    try:
        print(msg_0)
        calc = input()

        x, oper, y = calc.split()  # split calc into variables

        if x == "M":
            x = memory
        else:
            x = float(x)
        if y == "M":
            y = memory
        else:
            y = float(y)

        if oper not in ops:
            print(msg_2)
        else:
            check(x, y, oper)
            if oper == "+":
                result = float(x + y)
                print(result)
            elif oper == '-':
                result = float(x - y)
                print(result)
            elif oper == "*":
                result = float(x * y)
                print(result)
            elif oper == "/":
                result = float(x / y)
                print(result)

            # Store Result?
            while True:
                print(msg_4)  # Store Result?
                answer = input()
                if answer == "y":
                    if is_one_digit(result):
                        msg_index = 0
                        asking = True
                        while asking:
                            print(checks[msg_index])
                            answer = input()
                            if answer == "y":
                                if msg_index == 2:
                                    memory = result
                                    asking = False
                                msg_index += 1
                            if answer == "n":
                                asking = False
                        break
                    else:
                        memory = result
                        break
                elif answer == "n":
                    break

            # Continue Calculations?
            while True:
                print(msg_5)
                answer = input()
                if answer == "y":
                    break
                elif answer == "n":
                    running = False  # wrap it up!
                    break

    except ValueError:
        print(msg_1)
    except ZeroDivisionError:
        print(msg_3)
