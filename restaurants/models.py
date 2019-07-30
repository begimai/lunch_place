from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=300)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish = models.CharField(max_length=200)


class Employee(models.Model):
    name = models.CharField(max_length=200)
    employment_date = models.DateField('date employed')


class Vote(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
