from django.db import models
#from address.models import AddressField
from django.core.exceptions import ValidationError
import datetime
# Create your models here.

def rating_validator(value):
    if value>5 or value<0:
        raise ValidationError(
            '%(value) must be between 0 and 5'
    )

JOB_AT=[
    ('Google','Google'),
    ('Apple','Apple')
]

FACULTY=[
    ('BCT', 'Bachelor in Computer Engineering'),
    ('BEX', 'Bachelor in Electronics Engineering'),
    ('BCE', 'Bachelor in Civil Engineering'),
    ('BME', 'Bachelor in Mechanical Engineering'),
    ('BArch', 'Bachelor in Architecture'),
]

import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Subject(models.Model):
    name=models.CharField(max_length=20)
    code=models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Address(models.Model):
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.state + " state" + ", " + self.country 


class University(models.Model):
    objects=models.Manager()
    name=models.CharField(max_length=50)
    address=models.ForeignKey(Address, on_delete=models.CASCADE)
    rank=models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    objects = models.Manager()
    name=models.CharField(max_length=50)
    gmail_id=models.EmailField(max_length=50)
    bachelor_degree=models.CharField(choices=FACULTY, max_length=50)
    permanent_address=models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address_permanent')
    current_address=models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address_temporary')
    photo=models.ImageField()
    rating=models.IntegerField(validators=[rating_validator])
    year_passed=models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    year_enrolled=models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    scholarship=models.CharField(max_length=50)
    university=models.ForeignKey(University, on_delete=models.CASCADE)
    job_at=models.CharField(max_length=50, choices=JOB_AT)
    job=models.CharField(max_length=50, default="None")
    
    def __str__(self):
        return self.name

