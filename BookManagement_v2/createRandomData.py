import sys
sys.path.append("..")

import random
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

character = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

count = 0

while count < 1000:
    bookName = ""
    authorName = ""
    nameLength = random.randint(10, 20)
    for i in range(nameLength):
        bookNameLength = random.randint(0, 51)
        authorNameLength = random.randint(0, 51)
        bookName += character[bookNameLength]
        authorName += character[authorNameLength]
    categoryIndex = random(1, data.categoryListLength)
    category = data.categoryList[categoryIndex]
    score = random.randint(0, 9) + round(random.random(), 2)
    tempBookInfo = [bookName, authorName, category, score, time.time()]
    bookInfo = service.createBookInfo(tempBookInfo)
    dataInput = service.createDictFromList(data.bookKeys, bookInfo)
    model.addNewBook(dataInput)
    count += 1
    