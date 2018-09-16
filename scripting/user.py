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
    def addEntryOnDate(self, date, recipe, resource):
        self.sheet = self.sheet.append({'date': date, 'recipe': recipe, 'resource': resource}, ignore_index=True)
        self.writeFile()
    def addEntry(self, recipe, resource):
        self.addEntryOnDate(datetime.datetime.today(), recipe, resource)
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


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


if __name__ == '__main__':
    userid = '0001'
    user = userHandler(userid)
    # user.addEntry("funnyStuffdsa", 25)
    print(user.getConsumptionDay())
    print(user.getConsumptionWeek())
    print(user.getConsumptionMonth())
    print(user.getConsumptionYear())

    # ADD DATA TO USER DB
    # from datetime import timedelta, date
    # from numpy.random import normal
    # import random
    # recipeList = ['ceasar salad', 'chicken alfredo',
    # 'chicken fried rice',
    # 'chili con carne',
    # 'chili sin carne',
    # 'fried rice',
    # 'fruit salad',
    # 'lamb chops',
    # 'lentil soup',
    # 'meat breakfast',
    # 'meat curry',
    # 'meat pizza',
    # 'meat snack',
    # 'mixed salad',
    # 'pasta bolognese',
    # 'potato soup',
    # 'vegan bolognese',
    # 'vegan breakfast',
    # 'vegan curry',
    # 'vegan pizza',
    # 'vegan snack',
    # 'vegetable soup',
    # 'vegetarian breakfast',
    # 'vegetarian pizza',
    # 'vegetarian snack']
    #
    # mu = 3500.0
    # sigma = 500
    # start_date = date(2018, 1, 1)
    # end_date = date(2018, 9, 16)
    # for single_date in daterange(start_date, end_date):
    #     print(single_date.strftime("%Y-%m-%d"))
    #     for x in range(3):
    #         impact = normal(mu, sigma, 1)[0]/3
    #         food   = random.choice(recipeList)
    #         user.addEntryOnDate(single_date, food, impact)
    #         print(food, impact)