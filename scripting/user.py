import pandas as pd
import datetime


class userHandler:
    def __init__(self, userid):
        self.__fpath = '../data/user.xls'
        self.userid = userid
        xls = pd.ExcelFile(self.__fpath)
        self.sheet = pd.read_excel(xls)
    def writeFile(self):
        writer = pd.ExcelWriter(self.__fpath)
        self.sheet.to_excel(writer, self.userid)
        writer.save()
    def addEntry(self, recipe, resource):
        self.sheet = self.sheet.append({'date': datetime.datetime.today(), 'recipe': recipe, 'resource': resource}, ignore_index=True)
        self.writeFile()
    def getConsumptionDay(self):
        some = self.sheet[self.sheet['date'],:]
        return 500
    def getConsumptionWeek(self):
        return 5000
    def getConsumptionMonth(self):
        return 50000
    def getConsumptionYear(self):
        return 500000


if __name__ == '__main__':
    userid = '0001'
    user = userHandler(userid)
    # user.addEntry("funnyStuffdsa", 25)
    print(user.getConsumptionDay())
    print(user.getConsumptionWeek())
    print(user.getConsumptionMonth())
    print(user.getConsumptionYear())
