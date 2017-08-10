#!/usr/bin/env python3

STRING_1 = 'Hello'
STRING_2 = 'World'
NUMBER_1 = 3.1456
NUMBER_2 = 412499.35
LIST = ['Aldi']
# LIST = ['Amazon', 'Walmart', 'Gaint Eagle', 'Costco']
print(STRING_1)
print(STRING_2)
print('{} {}' .format(STRING_1, STRING_2))
print ('{} {}' .format(STRING_1, NUMBER_1))
print ('This is an way to print pi ' + str(NUMBER_1) + ' With ' + STRING_1)
print ('This is an other way {:.2f} with {}' .format(NUMBER_1, STRING_1))
print (NUMBER_1, NUMBER_2)
print (NUMBER_1 * NUMBER_1)
print("{} {} on my list".format(
    len(LIST),
    "store" if len(LIST) == 1 else "stores",
))
