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
    def __sumStuff__(self, tmpdf):
        return tmpdf['resource'].sum()
    def getConsumptionDay(self):
        some = self.sheet[self.sheet['date'] >= datetime.datetime.today().strftime("%Y-%m-%d")]
        return self.__sumStuff__(some)
    def getConsumptionWeek(self):
        some = self.sheet[self.sheet['date'] >= str(datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().weekday()))]
        return self.__sumStuff__(some)
    def getConsumptionMonth(self):
        some = self.sheet[self.sheet['date'] >= datetime.datetime.today().replace(day=1).strftime("%Y-%m-%d")]
        return self.__sumStuff__(some)
    def getConsumptionYear(self):
        some = self.sheet[self.sheet['date'] >= datetime.datetime.today().replace(day=1).replace(month=1).strftime("%Y-%m-%d")]
        return self.__sumStuff__(some)


if __name__ == '__main__':
    userid = '0001'
    user = userHandler(userid)
    # user.addEntry("funnyStuffdsa", 25)
    print(user.getConsumptionDay())
    print(user.getConsumptionWeek())
    print(user.getConsumptionMonth())
    print(user.getConsumptionYear())
