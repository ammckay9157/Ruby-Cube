# Hey there! My name is Andrew, and I'll be creating the updated framework for Ruby.

"""Ruby the Cube"""
__author__ = "Andrew McKay"


# This code is designed to explain the program to the user in a narrative way.
def help_command():
    print("The purpose of this program is to help any users that may stumble onto it.")
    print("My primary directive is to function as a codex.")
    print("In other words, given a word or name, I will give you the information I have on it.")
    print("My information will be as objective as possible, but I was created from the memories of Ruby.")
    print("Some words will cause me to execute code, while others will pull up the information I have")
    print("on an entity.")
    return


def calculate():
    calculator = input("Please enter which mode you would like to use: add, subtract, multiply, divide").lower()

    if calculator == "add":
        add_1 = float(input("Please input the first number you'd like to add."))
        add_2 = float(input("Please input the second number you'd like to add."))
        addition = add_1 + add_2
        print(addition)

    elif calculator == "subtract":
        sub_1 = float(input("Please input the first number you'd like to have be subtracted."))
        sub_2 = float(input("Please input the second number you'd like to use to subtract."))
        subtraction = sub_1 - sub_2
        print(subtraction)

    elif calculator == "multiply":
        mul_1 = float(input("Please input the first number to be multiplied."))
        mul_2 = float(input("Please input the second number to be multiplied."))
        multiply = mul_1 * mul_2
        print(multiply)

    elif calculator == "divide":
        div_1 = float(input("Please input the number to be the dividend."))
        div_2 = float(input("Please input the second number to be the divisor."))
        divide = div_1 / div_2
        print(divide)

    else:
        calculator = input("Then instead use modulo, floor division, exponent, or none.")
        # This program was split to help keep the number of characters on one line lower.

    if calculator == "modulo":
        mod1 = float(input("Please input the number to be modified."))
        mod2 = float(input("Please input the modulus number base."))
        modular = mod1 % mod2
        print(modular)

    elif calculator == "floor division":
        flr_div_1 = float(input("Please input the dividend."))
        flr_div_2 = float(input("Please input the divisor."))
        floor_division = flr_div_1 // flr_div_2
        print(floor_division)

    elif calculator == "exponent":
        base = float(input("Please input the base."))
        exp = float(input("Please input the power the base is to be raised to."))
        exponent = base ** exp
        print(exponent)

    else:
        print("Then why did you even ask me to calculate anything? Screw you.")


print("Hello, user. My name is Ruby. What would you like to ask me today?")
print("Type 'help' for a guide on how to use this program.")

user_command_1 = input("Type out a command.")

if user_command_1.lower() == "help":
    help_command()


if user_command_1.lower() == "stephen":
    print("Ah, you mean the master of the dungeon? I once knew him quite well, personally. Now, however, "
          "we are distant.")
    print("After all, the body of the one I was made to replicate has died from the Death Curse.")
    print("Stephen is a Reaper, and in a different timeline he was the King of Terra. Now, I believe he rules"
          " all in a unique way.")
    print("I personally do not like him, nor do I trust him or Lou.")

if user_command_1.lower() == "lou":
    print("I do not trust her. She is selfish, and technically she stole my husband and children from me.")
    print("If my body was able, it would strangle that woman. It was probably my plan.")

if user_command_1.lower() == "jessica":
    print("Jessica is an android created by Acererack for the explicit purpose of leading adventurers")
    print("to the Lost City. Her original designation was Jar 256. She is designed to seem like a source")
    print("of help to adventurers searching for Acererack's tomb. In reality, upon setting foot in the")
    print("Lost City, she is programmed to transform into a nuclear warhead that detonates in 30 minutes.")
    print("The only way to survive is to head into the tomb, the only place designed to withstand")
    print("the blast of a nuclear explosion. Upon destruction, another android is surfaced.")

if user_command_1.lower() == "acererack":
    print("Acererack killed me on the third level of his dungeon. I found no weaknesses in the archlich.")
    print("I did notice that he is very confident in himself, but as his goal is to end the world,")
    print("I suppose it makes sense.")

if user_command_1.lower() == "andrew":
    print("Yes, I've spoken to him in the past. I'm guessing you know him as well. Curse math.")

if user_command_1.lower() == "riley":
    print("Ah, which one do you mean? One is a dear friend, the other I've never met. The stranger seems")
    print("curious. I sense a potential in that one. He may become a mathematician one day.")

if user_command_1.lower() == "ruby":
    print("Me? I am an artificial intelligence recreated from the memories of Ruby.")

if user_command_1.lower() == "gfuel":
    print("This program was not sponsored by G-Fuel, but it certainly helped with the creation.")

if user_command_1.lower() == "math":
    calculate()

if user_command_1.lower() == "project z":
    print("Ah, you mean the OneNote project free for all to use? It's currently still in development.")
    print("Send a Discord message to EdgierPeach678#0877 to request access to the project.")
    print("Also, the password is: charlotte")

if user_command_1.lower() == "jack":
    print("Omu")

else:
    print("I'm sorry, I haven't heard of that.")

input('Press ENTER to exit')