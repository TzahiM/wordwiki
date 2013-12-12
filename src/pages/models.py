from django.db import models
from django.core.validators import MaxLengthValidator 

# Create your models here.

class Page(models.Model):
    name = models.CharField(unique = True, max_length=200, validators=[MaxLengthValidator])
    header = models.CharField(blank=True, max_length=200)
    create_date = models.DateTimeField('date created', auto_now_add=True )
    update_date = models.DateTimeField('last-modifie', auto_now =True )

    body_text = models.TextField(blank=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

