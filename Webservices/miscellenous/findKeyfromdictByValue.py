
# find key using given value
def getKeyfromvalue(dispDict, valuefind):

    #create emtpy list of keys
    listKeys = list()

    listDict = dispDict.items()

    # user iterate
    # for item in listDict:
    #     if item[1] == valuefind:
    #         listKeys.append(item[0])

    # using list comprehension
    findkey = [key for (key, value) in listDict if value == 12]
    return findkey

# find list of keys using given list of values
# filter the keys if given list of values matched


def getKeyfromvalues(dispDict, valuelistfind):

    #create emtpy list of keys
    listKeys = list()

    listDict = dispDict.items()

    # user iterate
    for item in listDict:
        # here item[1] is value and item[0] is key
        if item[1] in valuelistfind:
            listKeys.append(item[0])

    return listKeys



if __name__ == "__main__":

    # Create a dict from tuple
    listofTuples = [("Riti", 11), ("Aadi", 12), ("Sam", 13), ("John", 22), ("Lucy", 90)]
    dispDict = dict(listofTuples)

    # find key from given dict
    findkey = getKeyfromvalue(dispDict, 12)
    print findkey

    for i in findkey:
        print i

    # find list of key using given array of values
    findListKey = getKeyfromvalues(dispDict, [12, 22])
    print findListKey