from django.db import models

# Create your models here.
class Advisor(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Photourl = models.URLField()

    def __str__(self):
        return self.Name

class Users(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=256)

    def __str__(self):
        return self.Name

class CallBooked(models.Model):
    Id = models.AutoField(primary_key=True)
    Advisor = models.ForeignKey(Advisor,on_delete=models.CASCADE)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Time = models.TimeField()
    
    def __str__(self):
        return self.User.Name + "->" + self.Advisor.Name