'''
print even number from given range e.g 1 to 4
'''
import logging
logging.basicConfig(level=logging.DEBUG)


# find list of even number using for loop
def findEvenNum1(param):
    evenArray = []
    if param < 1:
        logging.debug ('Given number should be greater than 1')
    else:
        for i in range(1,param + 1):
            evenNum = i%2
            if evenNum == 0:
                evenArray.append(i)
            else:
                continue
        logging.debug ('List of Even numbers using for loop :' , evenArray)

# find list of even number using list comprehension
def findEvenNum2(param):

    evenArray = []
    [evenArray.append(x) for x in range (1, param + 1) if (x%2 == 0)]

    logging.debug ('List of Even numbers using list comprehension:' , evenArray)

# main method
if __name__ == "__main__":

    findEvenNum1(4)
    findEvenNum2(4)