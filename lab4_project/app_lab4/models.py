from django.db import models

# Create your models here.
class Student(models.Model):
    univ_id = models.CharField(max_length=70, blank=False, default='')
    first_name = models.CharField(max_length=70, blank=False, default='')
    last_name = models.CharField(max_length=70, blank=False, default='')
    course = models.CharField(max_length=70, blank=False, default='')
    age = models.IntegerField(blank=False, default=0)
    #published = models.BooleanField(default=False)
    #def save(self, *args, using=None, **kwargs):
     #   super(Room, self).save(*args, using='aip_building', **kwargs)