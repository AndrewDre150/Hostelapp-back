from django.db import models

# Create your models here.

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=120)
    location = models.CharField(max_length=255, default="Unknown")
    CATEGORY_CHOICES = (
        ('Single', 'Single'),
        ('Double', 'Double'),
    )
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(blank=True)
    security = models.BooleanField(default=False)
    shuttle = models.BooleanField(default=False)
    reading_room = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    contact = models.CharField(max_length=20)
    website = models.CharField(max_length=120)


    def _str_(self):
        return self.hostel_name