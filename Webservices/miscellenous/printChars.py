'''

Print each character in new line  for given array
Author: Javed
Date: Nov 20,2019
'''

import logging
logging.basicConfig(level=logging.DEBUG)

#  function 'printChar1'  input array list and print each item into new line using for loop
def printChar1(param):
    logging.debug('Print chars using for loop')
    for item in param:
        logging.debug(item)


#  function 'printChar2'  input array list and print each item into new line using join command
def printChar2(param):
    logging.debug('Print chars using join')
    logging("\n".join(param))

#  function 'printChar3'  input array list and print each item into new line using list comprehension using python 3

def printChar3(param):
    logging.debug('Print chars using comprehension')
    [logging.debug (x)  for x in param]

# main method
if __name__ == "__main__":
    listArray = ['a','b','c']
    printChar1(listArray)
    printChar2(listArray)
    printChar3(listArray)