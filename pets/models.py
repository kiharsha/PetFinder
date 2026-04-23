from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    PET_TYPE_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    pet_type = models.CharField(max_length=10, choices=PET_TYPE_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='pet_images/')
    is_lost = models.BooleanField(default=False)

    def __str__(self):
        return self.name