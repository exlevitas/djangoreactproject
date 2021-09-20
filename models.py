from django.db import models


class Customer(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address =  models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.first_name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    group = models.ForeignKey('Group', on_delete=models.PROTECT)
    course = models.ManyToManyField('Course')


class Group(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey('Course', on_delete=models.PROTECT)
    start = models.DateTimeField()
    end = models.DateField()

class Course(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    durations = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    description = models.TextField()