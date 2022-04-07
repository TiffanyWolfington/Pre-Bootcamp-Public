#def this is a function name # Snake case that's the nameing convention used in Python
def is_interger_weird(n): #n = Interger
    if n % 2 == 1: # 7 % 2 gives 1 because 7 / 2 gives us with a remainder of 1; 11 % 3 gives 2 since 11 / 3 = 3 with a remainder
        print("Weird")
    # Because we already checked to see whether the number was odd first, we don't need to check to see if the number is even here #because at this point it has to be even (assuming n is an interger) Thus order of logic is important!
    elif n <= 5 and n >= 2:
        print("Not Weird")
    #pass # we know we need to add code, but we don't know exactly what yet


# Make up some test cases
is_interger_weird(11)
is_interger_weird(20)