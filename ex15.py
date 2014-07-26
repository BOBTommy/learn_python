__author__ = 'riskkim'

from sys import argv #Import a module

script, filename = argv #Argument passing when run scripting

txt = open(filename) #Open File

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ") #Input -> > Something

txt_again = open(file_again) #Open again

print txt_again.read() #read and print