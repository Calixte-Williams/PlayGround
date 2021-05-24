#Input() : function allows program to ask user for more info and assignes entered info into a string variable/ date store.

#inpt = input('Type your name: ')
#print(inpt)

#Since Input() always saves as a String, you need to do a conversion to save as other data types. See Below example of a Float conversion.
#fltinpt = float(input('What is the Temperature in F: '))
#print(fltinpt)


'''Print() function is used to output info to user. At the end of every print() is a "\n" that signals a new line advance. 
This can be placed within a print() string to separate the lines.'''

print('Hello\nWorld')

""" 
You can use the following codes to control how text is displayed in a print()
//: Backslash
/b: Backspace
/': Single Quote
/": Double Quote
/t: Tab
/r: Carriage return
"""

#You can use the " sep='' " attribute to remove spaces between elemtents
numbs = {1,2,4,5,6,8,10}
print('Numbers in set', 1, ':', numbs )  #before attribute
print('Numbers in set', 1, ':', numbs, sep='')    #After attribute, notice all spaces between elements have been removed

#Adding in Python 3.6, f-string formatting, allows one to edit code faster and easier from the beginning of the line.
name = "Piper"
name2 = 'Chris'
print(name2,' says Hi to', name, '!')

print(f'{name2} says Hi to {name}!')      # Using f-string



