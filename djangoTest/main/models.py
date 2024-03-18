from django.db import models
import sqlite3


class DB():
    dbName = ''

    def __init__(self, dbName):
        self.dbName = dbName

    # connect = sqlite3.connect(dbName)
    # cursor = sqlite3.Cursor(connect)
    #
    # def createTown(self, name, id_country):
    #     self.cursor.execute(f'''INSERT INTO town id={NULL} , name={name} , id_country={id_country}''')
    #     self.connect.commit()
    #     self.connect.close()
    #
    # def selectTown(self):
    #     data = self.cursor.execute('''SELECT * FROM Town''')
    #     self.connect.fetchall(data)
    #     self.connect.close()
    #     return data
    #
    # def updateTown(self, name, id_country, id):
    #     self.cursor.execute(f'''UPDATE town name={name} , id_country={id_country}, WHERE id={id}''')
    #     self.connect.commit()
    #     self.connect.close()
    #
    # def deleteTown(self, id):
    #     self.cursor.execute(f'''DELETE town WHERE id={id}''')
    #     self.connect.commit()
    #     self.connect.close()


countTown = 0
countCountry = 0


class Town(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    id_country = models.CharField(max_length=200)

    def publish(self):
        global countTown
        self.id = countTown + 1
        self.save()

    def __str__(self):
        return (self.id, self.name, self.id_country)

    def create(self, name, id_country):
        self.name = name
        self.id_country = id_country

    def getID(self):
        return (self.id)

    def update(self, name, id, id_country):
        self.name = name
        self.id_country = id_country

    def delite(self, id):
        self.id = id


class Country(models.Model):
    id = models.CharField(primary_key=True,max_length=200)
    name = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    vize = models.BooleanField()
    price = models.FloatField()

    def publish(self):
        self.id = countCountry + 1
        self.save()

    def __str__(self):
        return (self.id, self.name, self.price, self.picture, self.vize)

    def create(self, name, price, picture, vize):
        self.name = name
        self.price = price
        self.picture = picture
        self.vize = vize

    def update(self, id, name, picture, vize, price):
        self.name = name
        self.price = price
        self.picture = picture
        self.vize = vize

    def delite(self, id):
        self.id = id
