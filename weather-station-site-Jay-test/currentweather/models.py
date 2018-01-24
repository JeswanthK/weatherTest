from django.db import models

# The models file is used for creating database schemas that you can use to query the database
class Weather(models.Model): #this creates a table
    temperature = models.CharField(max_length=250) #these create different rows in the table
    wind_speed = models.CharField(max_length=100)

class Users(models.Model):
    user = models.CharField(max_length=250)
    date = models.CharField(max_length=9)
