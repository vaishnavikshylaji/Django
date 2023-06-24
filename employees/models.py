from django.db import models

# Create your models here.


class Designation(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'designations'


class Employee(models.Model):
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=125, null=True)
    year_of_experience = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'employees'



