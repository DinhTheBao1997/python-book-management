import sys
sys.path.append("..")

import json
import time

from model.model import Model         
from view.view import View
from service.service import Service
from data.data import Data

model = Model()
view = View()
service = Service()
data = Data()

class Controller:
    def matchFunction(self, customerChoice):
        checkToExit = 0

        if (customerChoice == 1):
            option = view.printListByOption()
            if (option == 1):
                model.getDataFromDatabase()
            elif (option == 2):
                model.getDataFromDatabasePassExam()
            input("Press enter to continue...")
            checkToExit = True

        elif (customerChoice == 2):
            bookInfoExceptId = view.enterBookInfo()
            bookInfo = service.createBookInfo(bookInfoExceptId)
            dataInput = service.createDictFromList(data.bookKeys, bookInfo)
            bookInfoDisplay = dataInput
            dataInput = json.dumps(bookInfoDisplay)
            inputTime = bookInfoDisplay["Input date"]
            bookInfoDisplay["Input date"] = time.strftime("%d/%m/%Y",time.localtime(inputTime))
            print("Check the information: " + json.dumps(bookInfoDisplay, ensure_ascii=False))
            input("Press enter to continue...")
            model.addNewBook(dataInput)
            checkToExit = True

        elif (customerChoice == 3):
            categoryIndex = view.selectCategory()
            categorySelected = data.categoryList[categoryIndex]
            count = model.getDataByCategory(categorySelected)
            if (count == 0):
                print("Sorry! We don't have any book of categoy: " + categorySelected)
            input("Press enter to continue...")
            checkToExit = True

        elif (customerChoice == 4):
            result = 0
            categoryIndex = view.selectCategory()
            categorySelected = data.categoryList[categoryIndex]
            temp =  model.getCategoryAverageScore(categorySelected)
            if (temp[1] == 0):
                print("Sorry! We don't have any book of categoy: " + categorySelected)
            else:
                result = temp[0] / temp[1]
            print("The category " + categorySelected + " average scores: " + str(round(result, 2)))
            input("Press enter to continue...")
            checkToExit = True

        elif (customerChoice == 5):
            condition = service.findSortCondition()
            defaultListId = []
            matchConditionList  = service.scoresList(condition)
            idList = matchConditionList[0]
            scoreList = matchConditionList[1]
            topTableKeys = []
            topTableValues = []
            for i in range(10):                
                greatestNumberIndex = service.FindTopScores(idList,scoreList)
                defaultListId.append(idList[greatestNumberIndex])
                del idList[greatestNumberIndex]
                del scoreList[greatestNumberIndex]
            for i in range(len(defaultListId)):
                topTableKeys.append("No " + str(i + 1))
            for i in range(len(defaultListId)):
                topTableValues.append(model.getDataById(defaultListId[i]))
            topBookDict = service.createDictFromList(topTableKeys, topTableValues)
            customerChoice = view.selectTopTable()
            if (customerChoice == 1):
                print("_____________________________")
                temp = topBookDict.get("No 1")
                info = []
                for i in range(len(data.bookKeys)):
                    info.append(temp.get(data.bookKeys[i]))
                print("No 1 information:")
                view.printTopBookInfo(info)
                print("_____________________________")
            elif (customerChoice == 2):
                count = 1
                while count < 4:
                    print("_____________________________")
                    temp = topBookDict.get("No " + str(count))
                    info = []
                    for i in range(len(data.bookKeys)):
                        info.append(temp.get(data.bookKeys[i]))
                    print("No " + str(count) + " information:")
                    view.printTopBookInfo(info)
                    count += 1
                print("_____________________________")
            elif (customerChoice == 3):
                count = 1
                while count < 6:
                    print("_____________________________")
                    temp = topBookDict.get("No " + str(count))
                    info = []
                    for i in range(len(data.bookKeys)):
                        info.append(temp.get(data.bookKeys[i]))
                    print("No " + str(count) + " information:")
                    view.printTopBookInfo(info)
                    count += 1
                print("_____________________________")
            elif (customerChoice == 4):
                count = 1
                while count < 11:
                    print("_____________________________")
                    temp = topBookDict.get("No " + str(count))
                    info = []
                    for i in range(len(data.bookKeys)):
                        info.append(temp.get(data.bookKeys[i]))
                    print("No " + str(count) + " information:")
                    view.printTopBookInfo(info)
                    count += 1
                print("_____________________________")
            checkToExit = True

        elif (customerChoice == 6):
            print("Goodbye!!!")
            checkToExit = False

        return checkToExit