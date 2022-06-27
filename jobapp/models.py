from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.



class location(models.Model):
    name = models.CharField(max_length=334,null=True)
    
    def __str__(self):
        return self.name
    
class pakage(models.Model):
    choise=(
        
        ("1L TO 2L","1L TO 2L"),
        ("2L TO 3L","2L TO 3L"),
        ("3L TO 5L","3L TO 5L"),
        ("5L TO 7L","5L TO 7L"),
        ("7L TO 75L","7L TO 75L"),
        )
  
    limit = models.CharField(choices=choise, max_length=3434352,null=True) 
    
    
    def __str__(self):
        return self.limit
    
class jobsdis(models.Model):
    
    imformation = RichTextField()    
    pakages=models.ForeignKey(pakage,on_delete=models.CASCADE,null=True)
    locations=models.ForeignKey(location, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.imformation
    
    
    
class movee(models.Model):
    name=RichTextField()    
    lik = models.TextField(null=True)
    def __str__(self):
        return self.name
    
    
class komalji(models.Model):
    emailofk = models.EmailField(max_length=34443)
    password = models.CharField(max_length=4553)
    
    
    
