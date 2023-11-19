from django.db import models

# Create your models here.

class jobPosting(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary_lower = models.IntegerField()
    salary_upper = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=False)