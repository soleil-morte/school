from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    experiance = models.IntegerField(default=0)
    age = models.IntegerField()

    def __str__(self):
        return self.full_name
    

class Group(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    f_name = models.CharField(max_length=120)
    l_name = models.CharField(max_length=120)
    age = models.IntegerField()
    subject = models.ManyToManyField(Subject)
    group = models.ManyToManyField(Group)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return self.f_name
