from django.db import models
from django.urls import reverse

class Type(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Janr(models.Model):
    janr = models.CharField(max_length=30)

    def __str__(self):
        return self.janr

class Regisser(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

class Place(models.Model):
    row = models.IntegerField()
    place = models.IntegerField()

    def __str__(self):
        return f"(Ряд {self.row}, Место {self.place})"


class Time(models.Model):
    date_time = models.DateTimeField()

    def __str__(self):
        return format(self.date_time, "%d.%m.%y %H:%M")

class Concert(models.Model):
    name_concert = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    length = models.TimeField()
    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    janr = models.ForeignKey('Janr', blank=True, null=True, on_delete=models.PROTECT)
    regisser = models.ForeignKey('Regisser', blank=True, null=True, on_delete=models.PROTECT)
    date_time = models.ForeignKey('Time', on_delete=models.PROTECT)
    img = models.ImageField(upload_to='photo/', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.name_concert

class Ticket(models.Model):
    concert = models.ForeignKey('Concert', related_name='concert_name', on_delete=models.PROTECT)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    place = models.ForeignKey('Place', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"