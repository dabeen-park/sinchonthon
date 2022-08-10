from django.db import models
from django.contrib.auth.models import User
# Create your models here.

UNIV_CHOICES = (
        ('1','서강대학교'),
        ('2','연세대학교'),
        ('3','이화여자대학교'),
        ('4','홍익대학교'),
    )

Track_CHOICES = (
    ('1','백엔드'),
    ('2','프론트엔드'),
    ('3','기획/디자인'),
)


class Person(models.Model):
    
    university = models.CharField(max_length=5, choices=UNIV_CHOICES)
    name = models.CharField(max_length=20)
    track = models.CharField(max_length=10, choices=Track_CHOICES )
    smallTallk = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name