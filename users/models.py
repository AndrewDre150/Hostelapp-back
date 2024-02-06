from django.contrib.auth.models import AbstractUser, Group, Permission # Import Group
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # Add your custom fields here
    group = models.CharField(max_length=50)

    # Add related_name to groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='customuser_set',  # Add related_name
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_set',  # Add related_name
        related_query_name='user',
    )

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    college = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    student_number = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    # Add other fields as needed

    def __str__(self):
        return f"{self.name} {self.surname}"