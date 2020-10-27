class Extension(object):
    def viewDivision(self):
        print("Number division: ")
        print("1: 1;")
        for i in range(1, 1001):
            result = []
            for j in range(1, i + 1):
                if (i % j == 0):
                    result.append(j)
            print(str(i) + ": " + str(result))

extension = Extension()
extension.viewDivision()