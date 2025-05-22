from django.db import models
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField
    types=models.CharField(max_length=200,choices=(('Tech','Tech'),
                                                   ('Non Tech ','Non Tech'),
                                                   ('Others','Others')))
    

    def __str__(self):
        return self.name

    

    

# Create your models here.
    
class Empolyee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    about=models.TextField()
    address=models.CharField(max_length=200)
    position=models.CharField(max_length=20,choices=(('Manager','manager'),
                                                     ('Project Lead','pl'),
                                                     ('Software Developer','sd')))
    company_name=models.ForeignKey(Company,on_delete=models.CASCADE)

 

