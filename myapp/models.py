from django.db import models

# Create your models here
class enquiry_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class booking_table(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    phone=models.IntegerField()
    date=models.DateField(max_length=255)
    time=models.TimeField(max_length=255)
    people=models.IntegerField()
    message=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
