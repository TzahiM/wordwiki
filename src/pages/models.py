from django.core.urlresolvers import reverse
from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Page(models.Model):
    name = models.CharField(unique = True, max_length=200, validators=[MaxLengthValidator])
    header = models.CharField(blank=True, max_length=200)
    create_date = models.DateTimeField('date created', auto_now_add=True )
    update_date = models.DateTimeField('last-modifie', auto_now =True )

    body_text = models.TextField(blank=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
    def get_absolute_url(self):
        return( self.name)
#        return reverse('views.details',  args= [self.name])
    def as_html(self):
        lower_text = self.body_text.lower()
        words_list = lower_text.split()
        url_list = []
        for item in words_list:
            url_list.append( mark_safe ('<a href = "/word/' + item + '">' + item + '</a>'))
        return url_list
            

        