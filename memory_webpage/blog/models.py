from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
	task = models.CharField(max_length = 100, primary_key = True)
	studied_date = models.DateTimeField(default = timezone.now)
	first_review_date = models.DateTimeField(default = timezone.now)
	second_review_date = models.DateTimeField(default = timezone.now)
	third_review_date = models.DateTimeField(default = timezone.now)
	fourth_review_date = models.DateTimeField(default = timezone.now)
	fifth_review_date = models.DateTimeField(default = timezone.now)