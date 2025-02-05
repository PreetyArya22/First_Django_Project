from django.db import models
import datetime

# Create your models here.

class Person (models.Model):
  first_name = models.CharField(max_length=55)
  last_name = models.CharField(max_length=55)

class Musician(models.Model):
  first_name = models.CharField(max_length=55)
  last_name=models.CharField(max_length=55)
  instrument = models.CharField(max_length=55)
  
class Album(models.Model):
  artist = models.ForeignKey(Musician , on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  release_date = models.DateField()
  num_starts = models.IntegerField()

class Person_Choice(models.Model):
  SHIRT_SIZE = {
    "S" : "Small",
    "M" : "Medium",
    "L" : "Large", 
  }
  name = models.CharField(max_length=55)
  shirt_size = models.CharField(max_length=55 , choices=SHIRT_SIZE)


""" you can also use enumeration classes to define choices in a concise way: """

class Runner(models.Model):
  MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
  name = models.CharField(max_length=40)
  medal = models.CharField(blank=True , choices = MedalType ,  max_length=10)
  
class Fruit(models.Model):
  name = models.CharField(max_length=100 , primary_key=True)
  type= models.CharField(max_length=100 , default="false" )
  
class Category(models.Model):
  name = models.CharField(max_length=100)
  fruit = models.ForeignKey(Fruit  , on_delete=models.CASCADE , verbose_name="related fruit")
  
class Car(models.Model):
  model = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)

class Toyota(models.Model):
  car = models.OneToOneField(Car , on_delete= models.CASCADE , verbose_name="related car")
  
class Manufacture(models.Model):
  car = models.ManyToManyField(Toyota , verbose_name="related toyota")
  
  
""" Model methods """

class Human(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime

        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}"