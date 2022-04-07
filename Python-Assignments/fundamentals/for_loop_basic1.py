#basic
for a in range(151):
    print(a)
#multiples of 5
for b in range(5,1005,5):
    print(b)
#Counting, the Dojo Way
for x in range(1,101):
    if x%5==0 and x%10==0:
        print("Coding Dojo")
    elif x%5==0:
        print("Coding")
    else:
        print(x)
#Whoa. That Sucker's Huge
sum = 0
for total in range(0, 500001):
    if total % 2 != 0:
        sum += total
print(sum)
#Countdown by Fours
for p in range(2018, 0, -4):
    if p >=0:
        print(p)
#Flexible Counter
def counter(lowNum, highNum, mult):
    for c in range(lowNum, highNum+1):
        if c % mult == 0:
            print(c)

counter(2, 9, 3)
