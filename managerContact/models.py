from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# Models Person
class Person(models.Model):
    name_person = models.CharField(max_length=80)
    email = models.EmailField()
    # numbers = models.CharField(max_length=80)
    date_creation = models.DateTimeField("Date creation")
    
    def __str__(self):
        return self.name_person
    
    def is_recent(self):
        time = timezone.now()
        # check if date creation is between now and yesterday at the same time
        return time + datetime.timedelta(days=1) <= self.date_creation <= time
    

# Models Numbers
class NumberTel(models.Model):
    # Person 
    person = models.ForeignKey(Person,  on_delete=models.CASCADE)
    # Number
    other_number = models.CharField(max_length=80)
    
    def __str__(self) -> str:
        return self.other_number
    