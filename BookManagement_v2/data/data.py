import os
__fileName ="test.txt"
__fileDir = os.path.dirname(os.path.realpath('__file__'))
__fileLink = os.path.join(__fileDir,"data/database", __fileName)
fileLink = __fileLink
class Data:
    appName = "______________________Book Management Application______________________"
    functionList = ("View book's list", "Add new book", "Display by category", "View category average", "Top books in store", "Exit!")
    categoryList = ("Comic", "Detective", "Fiction", "Science", "Others")
    bookKeys = ('Id', 'Name', 'Author', 'Category', 'Scores', 'Input date')
    topBookKeys = ('Highest Score', 'Top 3', 'Top 5', 'Top 10')
    topBookKeysLength = len(topBookKeys)
    check = False
    functionListLength = len(functionList)
    categoryListLength = len(categoryList)
    bookKeysLength = len(bookKeys)
    bookScoreMax = 10
    examOption = ("True", "False")
