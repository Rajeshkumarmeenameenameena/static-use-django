from django.db import models

# Create your models here.
class patient(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=10)
    phoneno=models.CharField(max_length=12)
    address=models.CharField(max_length=20)
    datebirth=models.DateField()
    bloodgroup=models.CharField(max_length=10)
    datebirth=models.DateField()
    
    def __str__(self):
        return self.name
    
class homepage(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    
class studentlog(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    pass1=models.CharField(max_length=20)
    
