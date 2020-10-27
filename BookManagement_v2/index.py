import sys
sys.path.append("..")

from view.view import View
from controller.controller import Controller
from data.data import Data
data = Data()
view = View()
controller = Controller()

checkToExit = True

while checkToExit == True:
    customerChoice = view.printMenu()
    checkToExit = controller.matchFunction(customerChoice)