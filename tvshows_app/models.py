from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date

# Create your models here.

class ShowManager (models.Manager):
    def basic_validator(self, postData):

        received_date = postData["selected_date"]
        today = datetime.strftime(date.today(),'%Y-%m-%d')

        errors = {}
        #add keys and values to errors dictionary for each invalid field
        if len(postData["title"]) < 2:
            errors["title"] = "Show title needs to be atleast 2 characters"
        if len(postData["network"]) < 3:
            errors["network"] = "Show network needs to be atleast 3 characters"
        if postData["desc"]:
            if len(postData["desc"]) < 10:
                errors["desc"] = "Show description needs to be atleast 10 characters"
        if received_date > today:
            errors["release_date"] = "Show's release date must occur in the past"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    desc = models.TextField(default= "This is a really cool book")
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()


