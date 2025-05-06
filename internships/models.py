from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

class Internship(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    company_id = models.CharField(max_length=255,blank=True)
    role = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    work_type = models.CharField(max_length=50)  # e.g., remote, onsite
    skills = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    date_posted = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField()
    applicants = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    description = models.TextField()

    def __str__(self):
        return f"{self.company_name} - {self.role}"
