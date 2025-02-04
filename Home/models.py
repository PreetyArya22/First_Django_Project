from django.db import models
import datetime

# Create your models here.

# class Person (models.Model):
#   first_name = models.CharField(max_length=55)
#   last_name = models.CharField(max_length=55)

# class Musician(models.Model):
#   first_name = models.CharField(max_length=55)
#   last_name=models.CharField(max_length=55)
#   instrument = models.CharField(max_length=55)
  
# class Album(models.Model):
#   artist = models.ForeignKey(Musician , on_delete=models.CASCADE)
#   name = models.CharField(max_length=100)
#   release_date = models.DateField()
#   num_starts = models.IntegerField()

# class Person_Choice(models.Model):
#   SHIRT_SIZE = {
#     "S" : "Small",
#     "M" : "Medium",
#     "L" : "Large", 
#   }
#   name = models.CharField(max_length=55)
#   shirt_size = models.CharField(max_length=55 , choices=SHIRT_SIZE)


""" you can also use enumeration classes to define choices in a concise way: """

# class Runner(models.Model):
#   MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
#   name = models.CharField(max_length=40)
#   medal = models.CharField(blank=True , choices = MedalType ,  max_length=10)
  
# class Fruit(models.Model):
#   name = models.CharField(max_length=100 , primary_key=True)
#   type= models.CharField(max_length=100 , default="false" )
  
# class Category(models.Model):
#   name = models.CharField(max_length=100)
#   fruit = models.ForeignKey(Fruit  , on_delete=models.CASCADE , verbose_name="related fruit")
  
# class Car(models.Model):
#   model = models.CharField(max_length=100)
#   brand = models.CharField(max_length=100)

# class Toyota(models.Model):
#   car = models.OneToOneField(Car , on_delete= models.CASCADE , verbose_name="related car")
  
# class Manufacture(models.Model):
#   car = models.ManyToManyField(Toyota , verbose_name="related toyota")
  
""" Many to one relationship """

# class  Reporter (models.Model):
#   first_name = models.CharField(max_length=50)
#   last_name = models.CharField(max_length=50)
#   email = models.EmailField(unique=True)
  
#   def __str__(self):
#     return f"{self.first_name } {self.last_name}"
  
# class Articles(models.Model):
#   headline = models.CharField(max_length=200)
#   pub_Date = models.DateField()
#   reporters = models.ForeignKey(Reporter , on_delete=models.CASCADE)
  
#   def __str__(self):
#     return self.headline
  
#   class Meta:
#     ordering = ["headline"]
  
  
""" many to many relationship"""


# class Persons(models.Model):
#   name = models.CharField(max_length=120)
#   def __str__(self):
#     return self.name

# class Groups(models.Model):
#   name = models.CharField(max_length=120)
#   members = models.ManyToManyField(Persons)
  
#   def __str__(self):
#     return self.name 
  
# class Membership (models.Model):
#   persons = models.ForeignKey(Persons , on_delete=models.CASCADE)
#   groups = models.ForeignKey(Groups , on_delete=models.CASCADE)
  
#   date_joined = models.DateField()
#   invite_reason= models.CharField(max_length=64)
  
  
#   def __str__(self):
#     return str(self.persons.name)
  
  
""" Model methods """


class Human(models.Model):
  first_name = models.CharField(max_length=60)
  last_name = models.CharField(max_length=60)
  birth_date = models.DateField()
  
  def human_boomer_status(self):
    if self.birth_date<datetime.date(1945, 8, 1):
      return "Pre-boomer"
    elif self.birth_date<datetime.date(1965, 1, 1):
      return "Baby-boomer"
    else:
      return "Post boomer"
    
  @property
  def full_name(self):
    return f"{self.first_name} {self.last_name}"