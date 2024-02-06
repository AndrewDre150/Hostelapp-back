from django.db import models

# Create your models here.

class Booking(models.Model):
    given_name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    email = models.EmailField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    course = models.CharField(max_length=120)
    college_name = models.CharField(max_length=120)
    full_name = models.CharField(max_length=120)
    emergency_contact = models.CharField(max_length=20)
    confirmation = models.BooleanField(default=False, verbose_name="I confirm the information provided")
 

