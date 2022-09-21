from django.db import models

# Create your models here.

# Basic function that returns a username

# Test:


# class Username(models.Model):
#     username = models.CharField(max_length=30)
#     complete = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.username

# Actual Code:
class Grade(models.Model):
    # Database fields
    criterionA = models.IntegerField(default=0, null=True)
    criterionB = models.IntegerField(default=0, null=True)
    criterionC = models.IntegerField(default=0, null=True)
    criterionD = models.IntegerField(default=0, null=True)
    
class Subject(models.Model):
    # Database fields
    subjectname = models.CharField(max_length=30, null=True)
    score = models.ManyToManyField(Grade)

    def __str__(self):
        return self.subjectname

class User(models.Model):
    # Database Fields
    username = models.CharField(max_length=30, null=True)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.username
