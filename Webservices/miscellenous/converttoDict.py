
def printDict(text, dispDict):

    print ("******************")
    print ("\n" + text)
    for key, value in dispDict.items():
        print (key, " :: ", value)



if __name__== "__main__":
    '''
    1. Converting a list to dictionary with list elements as values in dictionary
and keys are enumerated index starting from 0 i.e. index position of element in list
    '''

    listOfStr = ["hello", "at", "test", "this", "here", "now"]
    listOfInt = [56, 10, 40, 30, 35, 41]

    dispDict = {i : listOfStr[i] for i in range(0, len(listOfStr))}

    printDict("Dictionary with same value ", dispDict)

    '''
    Using dictionary comprehension
    2. Convert a list to dictiionary with list elements as key in dictionary, all key values will be same

    '''

    dispDict = { i : 5 for i in listOfStr}
    printDict("Dictionary with list element as key and same value ", dispDict)

    '''
    3. Using dict.fromKeys()
    Converting a list into dictionary with list elements as keys. All dictionary values will be same as input value
    '''

    dispDict = dict.fromkeys(listOfStr, 1)
    printDict("Dictionary with list element as key and same value given as e.g. 1 ", dispDict)

    '''
    4. Using zip()
    Create a dictionary using two list (listofStr as key and listofInt as value)
    '''
    # create zip object

    zipObj = zip(listOfStr, listOfInt)
    dispDict = dict(zipObj)
    printDict("Dictionary with two list array using zip ", dispDict)

    '''
    5. Convert tuple into dictionary
    '''
    # List of tuples
    listofTuples = [("Riti", 11), ("Aadi", 12), ("Sam", 13), ("John", 22), ("Lucy", 90)]
    dispDict = dict(listofTuples)
    printDict("Convet Tuple into Dictionary ", dispDict)