import json
from django.urls import reverse
from django.db import models
from django.db.models.base import ModelState
from django.contrib.auth.models import User
from django.db.models.query import InstanceCheckMeta # new
from django.forms.models import model_to_dict



# Create your models here.
class Hobbies(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    def to_dict(self):
        return {
            'id': self.id,
            'name' : self.name,
        }

class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    photo = models.ImageField(null=True, blank=True,)
    dateOfBirth = models.CharField(max_length=255)
    hobbies = models.ManyToManyField(
        Hobbies, 
        related_name="userHobbies"
        )
    friends = models.ManyToManyField("Users", blank=True)
    
    def __str__(self):
        self.hobbies
        return f"{self.name}"
        
    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'city': self.city,
            'dateOfBirth': self.dateOfBirth,
            'hobbies': model_to_dict(self, fields=[field.name for field in self._meta.fields]),
         
        }

class Friend_Request(models.Model):
    from_user = models.ForeignKey(Users, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(Users, related_name="to_user", on_delete=models.CASCADE)