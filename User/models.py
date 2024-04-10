from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    
class Room(models.Model):
    room_number = models.CharField(max_length=50)
    floor = models.IntegerField()
    no_of_rooms = models.IntegerField()
    AC_CHOICES = [
        ('AC', 'AC'),
        ('Non-AC', 'Non-AC'),
    ]
    ac_type = models.CharField(max_length=10, choices=AC_CHOICES)
    is_booked = models.BooleanField(default=False)
    booked_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return self.room_number