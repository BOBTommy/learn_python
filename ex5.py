__author__ = 'riskkim'
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height *= 2.54
weight *= 0.45359237

print "Let's talk about %s." % name
print "He's %.2f cents meters tall." % height
print "He's %.2f kilo grams heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %.2f, and %.2f I get %.2f." % (
    age, height, weight, age + height + weight)