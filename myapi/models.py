from django.db import models

# Create your models here.

#Create Company Models
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(
        ('IT', 'IT'),
        ('Non-IT', 'Non-IT'),
        ('Mobile Phones', 'Mobile Phones'),
    ))
    date_added = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


#Employee Model
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.IntegerField(max_length=11)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(
        ('Manager', 'manager'),
        ('Software Developer', 'sd'),
        ('Project Leader', 'pl'),
        ('Django Developer', 'dj'),
        ('ML Engineer', 'ml'),
    ))

    def __str__(self):
        return self.name
