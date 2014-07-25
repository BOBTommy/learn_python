__author__ = 'riskkim'
formatter = "%r %r %r %r" #Format string used print method

print formatter % (1, 2, 3, 4) #Print 1, 2, 3, 4 -> print "%r %r %r %r" %(1,2,3,4)
print formatter % ("one", "two", "three", "four") #also same
print formatter % (True, False, False, True) #also same
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    'So I said goodnight.'
) #Single quotes, double qoutes are not matter.

print "%r %r %r %r" %(1,2,3,4)