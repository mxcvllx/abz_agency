from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    name = models.CharField(max_length=50, unique=True)
    employment_position = models.CharField(max_length=200)
    employment_start_date = models.DateTimeField(auto_now_add=False)
    salary = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.id) + ' Name: ' + self.name

