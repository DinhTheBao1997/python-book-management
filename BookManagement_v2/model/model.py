import sys
sys.path.append("..")

import json
import time
import io

from data.data import Data, fileLink
data = Data()

class Model:
    # Get Data From Database
    def getDataFromDatabase(self):
        try:
            fileOpen = io.open(fileLink, mode='r', encoding='utf-8')
            for line in fileOpen:
                item = json.loads(line)
                inputTime = item.get('Input date')
                item['Input date'] = time.strftime("%d/%m/%Y",time.localtime(inputTime))
                print(item)
        except IOError:
            print(fileLink)

    def getDataFromDatabasePassExam(self):
        try:
            fileOpen = io.open(fileLink, mode='r', encoding='utf-8')
            for line in fileOpen:
                item = json.loads(line)
                if (item.get("Id") % 3 == 0 and item.get("Id") % 2 == 1):
                    inputTime = item.get('Input date')
                    item['Input date'] = time.strftime("%d/%m/%Y",time.localtime(inputTime))
                    print(item)
        except IOError:
            print(fileLink)

    # Get Number of Books stored
    def countBookNumber(self):
        fileOpen = open(fileLink, 'r')
        count = 0
        for line in fileOpen:
            count = count + 1
        return count

    # Add New Data Into Database
    def addNewBook(self, tempBookInfo):
        try:
            result = tempBookInfo + "\n"
            fileOpen = io.open(fileLink, mode='a+', encoding='utf-8')
            fileOpen.write(result)
            fileOpen.close()
        except IOError:
            print('Error: cannot open this file')
        return
    
    # Get Data By Category
    def getDataByCategory(self, category):
        fileOpen = io.open(fileLink, mode='r', encoding='utf-8')
        item = ""
        count = 0
        for line in fileOpen:
            item = json.loads(line)
            if (item.get("Category") == category):
                inputTime = item.get('Input date')
                item['Input date'] = time.strftime("%d/%m/%Y",time.localtime(inputTime))
                print(json.dumps(item, ensure_ascii=False))
                count = count + 1
        return count

    # Get Category Average Scores
    def getCategoryAverageScore(self, category):
        fileOpen = io.open(fileLink, mode='r', encoding='utf-8')
        item = ""
        count = 0
        totalScore = 0
        for line in fileOpen:
            item = json.loads(line)
            if (item.get("Category") == category):
                totalScore = totalScore + item.get("Scores")
                count = count + 1
        result = [totalScore, count]
        return result

    # Count Amount of Books Quantify
    def countHighScoreBookNumber(self, count, condition):
        fileOpen = open(fileLink, 'r')
        for line in fileOpen:
            item = json.loads(line)
            if (int(item.get("Scores")) == condition):
                count += 1
        return count

    # Get Id by Scores
    def getIdByScore(self, condition):
        fileOpen = io.open(fileLink, mode='r', encoding='utf-8')
        item = ""
        idList = []
        scoreList = []
        count = 0
        for line in fileOpen:
            item = json.loads(line)
            if (item.get("Scores") >= float(condition)):
                idList.insert(count, item.get("Id"))
                scoreList.insert(count, item.get("Scores"))
                count = count + 1
        result = [idList, scoreList]
        return result

    # Get Data By Id
    def getDataById(self, id):
        fileOpen = io.open(fileLink, mode='r', encoding='utf-8')
        item = ""
        for line in fileOpen:
            item = json.loads(line)
            if (item.get("Id") == id):
                inputTime = item.get('Input date')
                item['Input date'] = time.strftime("%d/%m/%Y",time.localtime(inputTime))
                return item
