import sys
sys.path.append("..")
import time

from data.data import Data
from service.service import Service

data = Data()
service = Service()

class View():
    # Print Function Menu
    def printMenu(self):
        print(data.appName)
        print('Thank you for using our services')
        print('______________Function Menu______________')
        service.printListFromData(data.functionList, data.functionListLength)
        print('Please enter the number to select the function: \n')
        result = service.selectOption(data.functionListLength)
        if (result < data.functionListLength):
            print("The " + data.functionList[result - 1].lower() + "'s screen:")
        return result

    # Print List Option
    def printListByOption(self):
        print("Please choose the List's option: ")
        service.printListFromData(data.examOption, len(data.examOption))
        result = service.selectOption(len(data.examOption))
        return result

    # Enter Book Infomation
    def enterBookInfo(self):
        bookName = input("Enter the book's name: ")
        bookAuthor = input("Enter the book's author: ")
        bookCategory = ""
        scoresCheck = False
        print("Please enter the number to select the category: ")
        service.printListFromData(data.categoryList, data.categoryListLength)
        temp = service.selectOption(data.categoryListLength)
        bookCategory = data.categoryList[temp - 1]
        print("Enter the book's scores: ")
        bookScores = service.selectOption(data.bookScoreMax)
        inputDate = time.time()
        bookInfoExceptId = [bookName, bookAuthor, bookCategory, bookScores, inputDate]
        return bookInfoExceptId

    # Choose category by enter number
    def selectCategory(self):
        print("Please enter the number to select the category: ")
        service.printListFromData(data.categoryList, data.categoryListLength)
        result = service.selectOption(data.categoryListLength)
        return result - 1

    # Choose top table by enter number
    def selectTopTable(self):
        print("Please enter the number to select the top table display: ")
        service.printListFromData(data.topBookKeys, data.topBookKeysLength)
        result = service.selectOption(data.topBookKeysLength)
        return result

    # Print top book information
    def printTopBookInfo(self, info):
        for i in range(len(info)):
            print(data.bookKeys[i] + ": " + str(info[i]))
