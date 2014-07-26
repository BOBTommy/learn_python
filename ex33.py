__author__ = 'riskkim'

i = 0
numbers = []

def while_method(i):
    cursor = 0;
    while cursor < i:
        print "At the top i is %d" % cursor
        numbers.append(cursor)

        cursor += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % cursor

print "The numbers: "

while_method(6)

for num in numbers:
    print num