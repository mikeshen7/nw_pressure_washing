from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Contact(models.Model):
    description = models.CharField(max_length=500)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('contact_detail', args=[str(self.id)])