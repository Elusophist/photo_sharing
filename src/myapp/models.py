from django.db import models

class Pic(models.Model):
    picfile = models.ImageField()

#from django.urls import reverse

 #   class Meta:
  #      ordering = ['name',]

#class Resource(models.Model):
 #   show = models.BooleanField(default=True)
  #  thumbnail = models.ImageField(upload_to='resources/%Y/%m/%d/', null=True, blank=True)

#def get_absolute_url(self):
 #   return reverse('resource_detail', kwargs={'pk': self.id})

class share(models.Model):
    photo = models.ImageField()
