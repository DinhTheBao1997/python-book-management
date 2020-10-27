import sys
sys.path.append("..")

from model.model import Model
from data.data import Data
model = Model()
data = Data()

class Service(object):

    '''__________________View__________________'''
    # Print List From Data
    def printListFromData(self, list, listLength):
        for i in range(listLength):
            print(str(i + 1) + ". " + list[i])      
        return

    # Option
    def selectOption(self, limited):
        check = False
        customerChoice = 0
        while check == False:
            customerChoice_temp = input("Your choice: ")
            if (customerChoice_temp.isdecimal() == False):
                print("The input must be a number that greater than 0")
            else:
                customerChoice = int(customerChoice_temp)
                if (customerChoice > limited) or (customerChoice < 0):
                    print("Your choice is incorrect. The number must be in range: [0, " + str(limited)+ "]")
                else:
                    check = True
        return customerChoice

    '''__________________View__________________'''

    '''__________________Service__________________'''
    # Create Book Information
    def createBookInfo(self, tempBookInfo):
        temp = model.countBookNumber()
        if (temp == 0):
            nextId = 1
        else:
            nextId = temp + 1
        tempBookInfo.insert(0, nextId)
        return tempBookInfo

    # Create Dictionary From Two List
    def createDictFromList(self, keysList, valuesList):
        result = {}
        for i in range(len(keysList)):
            result.setdefault(keysList[i], valuesList[i])
        return result
    '''__________________Service__________________'''

    '''__________________Search__________________'''
    # Find a Required Scored to Sort
    def findSortCondition(self):
        count = 0
        check = False
        condition = 10
        while check == False:
            count = model.countHighScoreBookNumber(count, condition)
            if (count > 10):
                check = True
            else:
                condition = condition - 1
        return condition
        
    # Create Scores List to Sort
    def scoresList(self, condition):
        return model.getIdByScore(condition)
    # Find Top Scores
    def FindTopScores(self, idList, scoreList):    
        greatestNumber = scoreList[0]
        greatestNumberIndex = 0
        scoreListLength = len(scoreList)
        for i in range(scoreListLength):
            if (greatestNumber < scoreList[i]):
                greatestNumberIndex = i
                greatestNumber = scoreList[i]
            elif (greatestNumber == scoreList[i]):
                greatestNumberIndex = i
        return greatestNumberIndex

    '''__________________Search__________________'''
    