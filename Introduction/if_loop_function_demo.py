test_score = 95

if test_score >= 90:
    print("You did great! You got at least a 90!")
elif test_score >= 80:
    print("You did well! You got at least an 80!") # this will not print because the if statement is already true so it will ignore #this and move to next function.
print("End of if block")

x = [3, 5, 8]

for i in x:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
