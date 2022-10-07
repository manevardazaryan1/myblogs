from email.policy import default
from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    image = models.ImageField(upload_to='main/',null=True)
    owner = models.CharField('Owner',max_length=100)
    share = models.IntegerField('Share',default=0)
    
    def get_absolute_url(self):
        return f'/blogs/{self.id}'