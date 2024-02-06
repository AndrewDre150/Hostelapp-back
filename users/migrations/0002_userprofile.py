# Generated by Django 4.2.3 on 2023-11-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('college', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('student_number', models.CharField(max_length=20)),
                ('registration_number', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
            ],
        ),
    ]