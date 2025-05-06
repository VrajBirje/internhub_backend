from django.db import models
from users.models import User
from internships.models import Internship

class Application(models.Model):
    STATUS_CHOICES = [
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
    ]

    id = models.AutoField(primary_key=True)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    description = models.TextField(blank=True, null=True)
    resume_link = models.URLField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} - {self.internship.role}'
